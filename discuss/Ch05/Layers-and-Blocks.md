

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 20:52:58
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 20:53:16
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_deep-learning-computation/model-construction.html
 * @TODO::
 * @Reference:
-->

1 reply
8 Jul
Julia​Xu
To Q1, If changing MySequential to store blocks in a Python list, I got warning when call net.initialize():

UserWarning: “MySequential.blocklist” is an unregistered container with Blocks. Note that Blocks inside the list, tuple or dict will not be registered automatically. Make sure to register them using register_child() or switching to nn.Sequential/nn.HybridSequential instead.

Looks like the “list of blocks” is unregistered container and cannot be registered automatically. And the warning suggest that we can register_child manually. Following that, we can then get the same result as using the _children dictionary.

Here is the code:

class MySequential(nn.Block):

    def __init__(self, **kwargs):
        self.blocklist = []
        super().__init__(**kwargs)

    def add(self, block):
        self.blocklist = self.blocklist + [block]      # Change to list
        self.register_child(block, block.name)    # To fix issue: manually register child
        print(self.blocklist)

    def forward(self, x):
        for block in self.blocklist:
            x = block(x)
        return x
Continue Discussion

2 replies
26 Jun
anirudh
@kwang this is already fixed in master. It will be updated in the next release.
Also, it will just be

net = MySequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))
net(x)
3h
kusur
(post withdrawn by author, will be automatically deleted in 24 hours unless flagged)

Continue Discussion
