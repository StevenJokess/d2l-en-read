# https://github.com/xiaotinghe/alicloudPred/blob/master/inference/run.py
import flask
import pandas as pd
from mxnet import gluon, nd
from mxnet.gluon import nn, rnn
import numpy as np
app = flask.Flask(__name__)

class LSTNet(gluon.Block):
    def __init__(self, num_series, conv_hid, kernel_size, gru_hid, skip_gru_hid, skip, ar_window):
        super(LSTNet, self).__init__()
        kernel_size = kernel_size
        dropout_rate = 0.2
        self.skip = skip
        self.ar_window = ar_window
        with self.name_scope():
            self.conv = nn.Conv1D(conv_hid, kernel_size=kernel_size, layout='NCW', activation='relu')
            self.dropout = nn.Dropout(dropout_rate)
            self.gru = rnn.GRU(gru_hid, layout='TNC')
            self.skip_gru = rnn.GRU(skip_gru_hid, layout='TNC')
            self.fc = nn.Dense(72)
            self.ar_fc = nn.Dense(1)

    def forward(self, x):
        c = self.conv(x.transpose((0, 2, 1)))
        c = self.dropout(c)
        r = self.gru(c.transpose((2, 0, 1)))
        r = r[-1]  # Only keep the last output
        r = self.dropout(r)  # Now in NC layout
        # Skip GRU
        # Slice off multiples of skip from convolution output
        skip_c = c[:, :, -(c.shape[2] // self.skip) * self.skip:]
        skip_c = skip_c.reshape(c.shape[0], c.shape[1], -1, self.skip)  # Reshape to NCT x skip
        skip_c = skip_c.transpose((2, 0, 3, 1))  # Transpose to T x N x skip x C
        skip_c = skip_c.reshape(skip_c.shape[0], -1, skip_c.shape[3])  # Reshape to Tx (Nxskip) x C
        s = self.skip_gru(skip_c)
        s = s[-1]  # Only keep the last output (now in (Nxskip) x C layout)
        s = s.reshape(x.shape[0], -1)  # Now in N x (skipxC) layout
        # FC layer
        fc = self.fc(nd.concat(r, s))  # NC layout
        new_x = x
        res = []
        # Add autoregressive and fc outputs
        for i in range(fc.shape[1]):
            ar_x = new_x[:, -self.ar_window:, :]
            ar_x = ar_x.transpose((0, 2, 1))  # NCT layout
            ar_x = ar_x.reshape(-1, ar_x.shape[2])  # (NC) x T layout
            ar = self.ar_fc(ar_x)
            ar = ar.reshape(new_x.shape[0], -1)  # NC layout
            c_res = fc[:,i].expand_dims(1) + ar
            new_x = nd.concat(new_x, c_res.expand_dims(1), dim= 1)
            res.append(c_res)
        return nd.concat(*res, dim=1)
net = LSTNet(num_series=1, conv_hid=16, kernel_size = 6, gru_hid=4, skip_gru_hid=16, skip=16, ar_window=24)
net.load_parameters('net.params')

@app.route("/predict", methods=["GET","POST"])
def predict():
    resource_id = flask.request.form['resource_id']
    history_data = flask.request.form['history_data']
    history_data = nd.array([float(c) if c!= 'NA' else 0.0 for c in history_data.split(',')])
    data = dict()
    if len(history_data) < 24:
        data["resource_id"] = resource_id
        data["predict_data"] = ""
        data["message"] = "Historical data needs to be greater than 24"
        return flask.jsonify(data)
    x_mean, x_var = nd.moments(history_data, axes=0)
    x_std = nd.sqrt(x_var)
    X = (history_data - x_mean.expand_dims(1))/x_std.expand_dims(1)
    pred = net(X.expand_dims(-1))
    Y = (pred * x_std + x_mean).reshape(-1).asnumpy().tolist()
    data["resource_id"] = resource_id
    data["predict_data"] = ','.join(list(map(lambda y:str(round(y,2)), Y)))
    return flask.jsonify(data)

app.run(host='0.0.0.0', port='5000')
