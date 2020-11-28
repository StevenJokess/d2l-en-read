

###
 # @version:
 # @Author:  StevenJokess https://github.com/StevenJokess
 # @Date: 2020-11-28 00:51:59
 # @LastEditors:  StevenJokess https://github.com/StevenJokess
 # @LastEditTime: 2020-11-28 00:52:00
 # @Description:
 # @TODO::
 # @Reference:https://github.com/lanpa/tensorboardX/blob/master/run_pytest.sh
###
pip install pytest boto3 moto onnx tensorboard matplotlib flake8==3.8.3

if [ `ps|grep visdom |wc -l` = "1" ]
    then
    echo `ps|grep visdom |wc -l`
    echo "no visdom"
    visdom &
fi

PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python pytest

pytest tests/tset_multiprocess_write.py
