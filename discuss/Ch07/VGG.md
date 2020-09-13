6 replies
22 Aug
Nish
I was wondering if anyone can help me with a weird bug I’ve encountered. I’ll try to summarise. I’m training the network on fashion-mnist images resized to be 96x96 in size. I’ve adjusted the architecture appropriately, the problem is pretty strange: if I define the optimizer first and then pass it into my training function:
https://discuss.d2l.ai/uploads/default/optimized/1X/8585827b2d5964337eacb228a9f9869905094ce9_2_507x375.jpeg

optimizer=torch.optim.SGD(net.parameters(), lr=lr)
train(net, all_iter, test_iter, num_epochs, lr, optimizer)
The training breaks:
image
But if I copy-paste the exact same line of code that defines the optimizer inside the train function, and change nothing else:

def train(net, train_iter, test_iter, num_epochs, lr, optimizer=None, device=d2l.try_gpu()):
  optimizer = torch.optim.SGD(params=net.parameters(), lr=lr)
  ...
Then it works fine:

image
Here is my train function code - same as d2l basically, I just wanted to type it out myself:

def train(net, train_iter, test_iter, num_epochs, lr, optimizer=None, device=d2l.try_gpu()):
    """
    Trains a network 'net'. Assumes that net.init_weights exists
    """
    # 1: initialise weights
#     net.apply(net.init_weights)
    def init_weights_test(m):
        if type(m) == nn.Linear or type(m) == nn.Conv2d:
            torch.nn.init.xavier_uniform_(m.weight)
    net.apply(init_weights_test)

    # 2: move model to device for training
    net.to(device)

    # 3: set up optimizer, loss function, and animation stuff
    loss = nn.CrossEntropyLoss()
#     optimizer = torch.optim.Adam(params=net.parameters(), lr=lr)
    if optimizer is None:
        optimizer = torch.optim.SGD(params=net.parameters(), lr=lr)
    animator = d2l.Animator(xlabel="epoch number", xlim=[0, num_epochs], legend=["train loss", "train acc", "test acc"])

    # 4: training loop
    for epoch in range(num_epochs):
        metric = d2l.Accumulator(3)
        for i, (X, y) in enumerate(train_iter):
            X, y = X.to(device), y.to(device)
            net.train()
            optimizer.zero_grad()
            y_hat = net(X)
            l = loss(y_hat, y)
            l.backward()
            optimizer.step()
            # temporarily disable grad to calculate metrics
            with torch.no_grad():
                train_loss = l
#                 import ipdb; ipdb.set_trace()
                _, preds = torch.max(y_hat, 1)
                train_acc = ((preds == y).sum()) / float(X.shape[0])
            if (i + 1) % 50 == 0:
                animator.add(epoch + (i / len(train_iter)), (train_loss, train_acc, None))
        test_acc = evaluate_accuracy_gpu(net, test_iter, device)
        animator.add(epoch + 1, (None, None, test_acc))

    print(f'loss {train_loss:.3f}, train acc {train_acc:.3f}, test acc {test_acc:.3f}')
The only thing I’m training is not passing in a value for the optimizer parameter so that it takes the default value of None and is set inside the function body.

Any idea why this could cause an issue?

https://discuss.d2l.ai/uploads/default/original/1X/8a5b8f9295a4fdc8685aafce66082712228f9b4b.png

1 reply
23 Aug▶ Nish
Steven​Jokes
Can you publish all your code, and throw me a github URL?
I still wonder the part that you don’t show.
@Nish

1 reply
24 Aug▶ StevenJokes
Nish
Ok, I figured it out, I was just being stupid. Basically was doing something like this:

optimizer = optimizer(net)
net = net()
train(net, optimizer)
So of course the optimizer was not attached to the network. If you still want to laugh at my mistake you can read it all here https://github.com/NishantTharani/DeepLearning_CS231n_D2L/blob/master/d2l.ai/Ch7/vggnet.ipynb

1 reply
25 Aug▶ Nish
goldpiggy
Hey @Nish, you are not stupid. Asking questions is always smarter than hiding there. :wink:

25 Aug
Steven​Jokes
@Nish Wow, I learnt a lot from your github and know I need to learn more.
Have stared your repo. Keep going and communicating. :rofl:

25 Aug
Nish
Thank you both! I finished up with this chapter by testing out VGGNet 19 on our upscaled Fashion-MNIST - https://github.com/NishantTharani/LearningDeepLearning/blob/master/d2l.ai/Ch7/vggnet19.ipynb

image
Not bad!
https://discuss.d2l.ai/uploads/default/original/1X/e5f800c25eccea8ab6efceb65be1683d471a7bbc.png
Continue Discussion
