

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 21:27:49
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 21:29:02
 * @Description:https://github.com/apache/incubator-mxnet/issues/18931
 * @TODO::
 * @Reference:
-->
Skip to content
Search or jump to…

Pull requests
Issues
Codespaces
Marketplace
Explore

@StevenJokes
apache
/
incubator-mxnet
1.2k
19k
6.7k
Code
Issues
1.6k
Pull requests
177
Discussions
Actions
Projects
11
Wiki
Security
Insights
[Development] MXNet 2.0 Update #18931
 Open
szha opened this issue on Aug 15 · 27 comments
 Open
[Development] MXNet 2.0 Update
#18931
szha opened this issue on Aug 15 · 27 comments
Comments
@szha
Member
szha commented on Aug 15 •
Overview
As MXNet development approaches its 2.0 major milestone, we would like to update our community on roadmap status, and highlight new and upcoming features.

Motivation
The deep learning community has largely evolved independently from the data science and machine learning(ML) user base in NumPy. While most deep learning frameworks now implement NumPy-like math and array libraries, they differ in the definition of the APIs which creates confusion and a steeper learning curve of deep learning for ML practitioners and data scientists. This creates a barrier not only in the skillsets of the two different communities, but also hinders the knowledge sharing and code interoperability. MXNet 2.0 seeks to unify the deep learning and machine learning ecosystems.

What's new in version 2.0?
MXNet 2.0 is a major version upgrade of MXNet that provides NumPy-like programming interface, and is integrated with the new, easy-to-use Gluon 2.0 interface. Under the hood, we provide an enhanced DL implementation in NumPy. As a result, NumPy users can easily adopt MXNet. Version 2.0 incorporated accumulative learnings from MXNet 1.x and focuses on usability, extensibility, and developer experiences.

What's coming next?
We plan to make a series of beta releases of MXNet 2.0 in lockstep with downstream projects migration schedule. The first release is expected in September. Check back here or subscribe to dev@mxnet.apache.org for additional announcements.

How do I get started?
As a developer of MXNet, you can check out our main 2.0 branch. MXNet 2.0 nightly builds are available for download.

How can I help?
There are many ways you can contribute:

By submitting bug reports, you can help us identify issues and fix them.
If there are issues you would like to help with, let us know in the issue comments and one of the committers will help provide suggestions and pointers.
If you have a project that you would like to build on top of MXNet 2.0, post an RFC and let the MXNet developers know.
Looking for ideas to get started with developing MXNet? Check out the good-first-issues labels for Python developers and C++ developers
Highlights
Below are the highlights of new features that are available now in the MXNet 2.0 nightly build.

NumPy-compatible Array and Math Library
NumPy has long been established as the standard array and math library in Python and the MXNet community recognizes significant benefits in bridging the existing NumPy machine learning community and the growing deep learning community. In #14253, the MXNet community reached consensus on moving towards a NumPy-compatible programming experience, and committed to a major effort on providing NumPy compatible array library and operators.

To see what the new programming experience is like, check out Dive into Deep Learning book, the most comprehensive interactive deep learning book with code+math+forum. The latest version has an MXNet implementation with the new MXNet np, the NumPy-compatible math and array interface.

Gluon 2.0
Since the introduction of the Gluon API in MXNet 1.x, it has superseded other MXNet API for model development such as symbolic, module, and model APIs. Conceptually, Gluon was the first attempt in the deep learning community to unify the flexibility of imperative programming with the performance benefits of symbolic programming, through just-in-time compilation.

In Gluon 2.0, we are extending support to MXNet np with simplified interface and new functionalities:

Simplified hybridization with deferred compute and tracing: Deferred compute allows the imperative execution to be used for graph construction, which allows us to unify the historic divergence of NDArray and Symbol. Hybridization now works in simplified hybrid forward interface; users only need to specify the computation through imperative programming. Hybridization also works through tracing.
Data 2.0: The new design for data loading in Gluon allows hybridizing and deploy data processing pipeline in the same way as model hybridization. The new C++ data loader improves data loading efficiency on CIFAR 10 by 50%.
Distributed 2.0: The new distributed-training design in Gluon 2.0 provides a unified distributed data parallel interface across native Parameter Server, BytePS, and Horovod, and is extensible for supporting custom distributed training libraries.
Gluon Probability: parameterizable probability distributions and sampling functions to facilitate more areas of research such as Baysian methods and AutoML.
Gluon Metrics and Optimizers: refactored with MXNet np interface and addressed legacy issues.
3rdparty Plugin Support
Extensibility is important for both academia and industry users who want to develop new, and customized capabilities. In MXNet 2.0, we added the following support for plugging in 3rdparty functionality at runtime.

C++ custom operators: Enable operators to be implemented in separate libraries and loaded at runtime without re-compiling MXNet and maintaining MXNet fork.
Custom subgraph property for 3rdparty acceleration libraries: enable dispatching subgraphs to 3rdparty acceleration libraries that are plugged in at runtime.
Custom graph passes for 3rd party acceleration libraries: enable custom graph modification in C++ to enable fusing params, replacing operators, and other custom optimizations.
Developer Experiences
In MXNet 2.0, we are making development process more efficient in MXNet.

New CMake build system: improved CMake build system for compiling the most performant MXNet backend library based on the available environment, as well as cross-compilation support.
Memory profiler: the goal is to provide visibility and insight into the memory consumption of the MXNet backend.
Pythonic exception type in backend: updated error reporting in MXNet backend that allows directly defining exception types with Python exception classes to enable Pythonic error handling.
Documentation for Developers
We are improving the documentation for MXNet and deep learning developers.

CWiki for developers: reorganized and improved the development section in MXNet CWiki.
Developer Guide: new developer guides on how to develop and improve deep learning application with MXNet.
Ecosystem: GluonNLP NumPy
We are refactoring GluonNLP with NumPy interface for the next generation of GluonNLP. The initial version is available on dmlc/gluon-nlp master branch:

NLP models with NumPy: we support a large number of state-of-the-art backbone networks in GluonNLP including
BERT, ALBERT, ELECTRA, MobileBERT, RoBERTa, XLMR, Transformer, Transformer XL
New Data Processing CLI: Consolidated data processing scripts into one CLI.
API Deprecation
As described in #17676, we are taking this major version upgrade as an opportunity to address the legacy issues in MXNet 1.x. Most notably, we are deprecating the following API:

Model, Module, Symbol: we are deprecating the legacy modeling and graph construction API in favor of automated graph tracing through deferred compute and Gluon.
mx.rnn: we are deprecating the symbolic RNN API in favor of the Gluon RNN API.
NDArray: we are deprecating NDArray and the old nd API in favor of the NumPy-compatible np and npx. The NDArray operators will be provided as an optional feature potentially in a separate repo. This will enable existing users who rely on MXNet 1.x for inference to have an easy upgrade path as old models will continue to work.
Caffe converter and Torch plugin: both extensions see low usage nowadays. We are extending support in DLPack to better support interoperability with PyTorch and Tensorflow instead.
Related Projects
Below is a list of project trackers for MXNet 2.0.

MXNet 2.0: the tracking project for MXNet 2.0.
MXNet NumPy API: the goal is to provide full feature coverage for NumPy in MXNet with auto-differentiation and GPU support.
MXNet Website 2.0: the revamped MXNet official website for better browsing experiences.
np interface bug fixes: the goal is to address technical debts and performance issues in np and npx operators.
CI & CD ops and developer experience improvement: reduce the development overhead by upgrading the CI/CD infrastructure and toolchain to improve the stability of CI/CD and developer efficiency.
MXNet 2.0 JVM language binding redesign (#17783)
@apache/mxnet-committers feel free to comment or directly edit this post for updates in additional areas.

@szha szha added the RFC label on Aug 15
@szha szha pinned this issue on Aug 15
@StevenJokes
This comment was marked as off-topic.
Hide comment
@StevenJokes
StevenJokes 25 days ago Contributor
I'm a newbie. I'm learning d2l DCGAN.
And I try to translate to pytorch. Then I found it isn't same with tutorial in pytorch.org.
Which one is right?
My issue is here: Maybe our DCGAN have extra nn.BatchNorm2d(ndf)?
Still not finish my work: PR

BTW, I found .add in mxnet is easy to use than .add_module in pytorch, which must name a new layer.
But I have another problem: After we added a layer, it will exist next time?
If then, how to delete or change a layer? Or, more often we just create a new structure?

@szha
This comment was marked as off-topic.
Hide comment
@szha
szha 25 days ago Member Author
@StevenJokes for usage questions, feel free to use https://mxnet.apache.org/community/contribute#forum. RFC issues like this notify all mxnet developers automatically for any discussion so let's move this elsewhere.

@StevenJokes
This comment was marked as off-topic.
Hide comment
@StevenJokes
StevenJokes 25 days ago Contributor
And one more thing, the new d2l forum have no offical reply three days.
I'm a newbie. I'm trying to answer some, but I'm afraid to mislead others.
Please spare some time to answer some if you guys can.

I'm thinking that the forum is most important to get more new users and find pain spots when communicating.
The pytorch's friendly is caused by the saved discussions. But if we use our forum correctly, we will beat them.

Our discussion is just after the chapters' context. It will be more systemic.
And we should rule the dicussions to depulicate less.

My opinion here:

We must let others to know that you cared about them when using our framework.
And the efforts about code can be delayed a little, because we need to train the first wave users from tf and pytorch to let them get familiar to mxnet. Then they can train the next and next waves.
I think one reason why mxnet 1.0 failed is that we don't care others and give no reply to their questions in discuss.mxnet.io .

We need to discuss more mxnet details other than just throw a universal code or docs.

The old developers must spare your precious time to test all mxnet code and fix them ASAP.
The old developers must spare your precious time to answer questions ASAP when we adding pytorch and tensorflow context, to attract other tf and pytorch users to coming.
And we should give them reasons why our framework is good after finishing replying.

d2l is the our only book, and we can find at least 5 books of pytorch and tensorflow.
If we don't grasp this chance, d2l will just help pytorch and tf developing and make mxnet more deadly.

All my thoughts.

@StevenJokes
This comment was marked as off-topic.
Hide comment
@StevenJokes
StevenJokes 25 days ago Contributor
Don't joke.
Please look https://discuss.mxnet.io/ again.
I ask you how many questions replied here these two months.
Then you can contrast it with discuss.pytorch.org

If we don't have many users, we should pay more attention to them and try to answer every questions.
Then more new users will come, because they know they can find others' solutions and if they can't, they are still cared about to be answered.

@StevenJokes
This comment was marked as off-topic.
Hide comment
@StevenJokes
StevenJokes 25 days ago Contributor
image

VS

image

Just imagine you are new user now. Which framework you will learn and which forum you will ask?

Why astonZhang and mli never answer questions in d2lbook?
Are they afraid that the answer will destroy our unsupervised learning?

@szha
This comment was marked as off-topic.
Hide comment
@szha
szha 25 days ago Member Author
@StevenJokes thanks for the feedback and I'm really glad that you feel strongly about mxnet and want it to get better. I share the sentiment and as a community I think this is indeed an area where we try to improve. cc @astonzhang on the d2l support. cc @sandeep-krishnamurthy

That said, the past few comments have been off-topic, and I will mark them so once others have a chance to look at them.

@qqaatw
This comment was marked as off-topic.
Hide comment
@qqaatw
qqaatw 25 days ago
I think one reason why mxnet 1.0 failed is that we don't care others and give no reply to their questions in discuss.mxnet.io .

@StevenJokes Thank you for mentioning this notable and important point! I perceive that an open source project should has an active community to grow up. The forum of MXNet is really inanimate, almost no experienced developers answer the questions on it. This situation will strongly reduce people’s desire to use this framework. Please try to improve it! Tks.

@szha
This comment was marked as off-topic.
Hide comment
@szha
szha 25 days ago Member Author
@qqaatw thank you for sharing your feedback. Again, I share the same sentiment and I myself will at least try to help as much as my bandwidth allows. That said, the proper channel to bring this up is a separate thread on dev@mxnet.apache.org.

This issue is for feedback on 2.0 features and use cases and I request that we stay on topic. I will mark these conversations as off-topic once others have a chance to look at them.

@StevenJokes
This comment was marked as off-topic.
Hide comment
@StevenJokes
StevenJokes 25 days ago Contributor
Off-topic again...
I hate yours' saying. The most important reason that I'm here is just to talk to all your developers.

@szha
This comment was marked as off-topic.
Hide comment
@szha
szha 25 days ago Member Author
@StevenJokes you still can reach developers by joining discussion on dev@mxnet.apache.org, or mentioning this team in GitHub @apache/mxnet-committers. They should happen in a different issue and thread, not here.

@StevenJokes
This comment was marked as off-topic.
Hide comment
@StevenJokes
StevenJokes 25 days ago Contributor
And you, developers, just feel good to keep mysterious until nobody understand your "nice" tool, abandon it and don't need you.
You don't need to forgive my very rude grumbles. Just to find some DL books to know that which frameworks most users will learn and talk about. And you can feel free to play your fascinating tools all your life.

I don't care whether it is right issue or not. I just alarm you guys here.

@StevenJokes
This comment was marked as off-topic.
Hide comment
@StevenJokes
StevenJokes 25 days ago Contributor
You should know that not all users have time and knowledge to read rules and follow your d2l systemic book.
Make your rules simple and obvious next time.

@qqaatw
This comment was marked as off-topic.
Hide comment
@qqaatw
qqaatw 25 days ago
@szha I was in the dev mailing list months ago, and I’m not really a new. BUT what @StevenJokes said really make sense, it is the most important thing, even the fatal problem on MXNet. Please do not put this matter aside, or a off-topic. Thank you for understanding in advance

@analog-cbarber
This comment was marked as off-topic.
Hide comment
@analog-cbarber
analog-cbarber 25 days ago
@StevenJokes, I am not involved in mxnet in any way. Your comments are really crossing over the line. While it is fair to point out that mxnet can be doing a better job reaching out to its intended community, this is not the place to do it. If I were you, I really would not want unprofessional comments such yours to be appearing where potential employers can find them.

@sxjscience
This comment was marked as off-topic.
Hide comment
@sxjscience
sxjscience 25 days ago Member
@StevenJokes I think the issue about DCGAN is related to D2L and you'd better to discuss it in the D2L-related channels. (Find one in the D2L: d2l-ai/d2l-en#1381) If you have specific issues about MXNet, you may create an issue and tag it as BUG, or other labels so we can take a look.

@StevenJokes
This comment was marked as off-topic.
Hide comment
@StevenJokes
StevenJokes 25 days ago Contributor
My summary is here:
image

OK. If you don't care me, I don't care you either.

@szha szha mentioned this issue 25 days ago
Discussion on Community Management #18963
 Open
@szha
Member
Author
szha commented 25 days ago
@qqaatw this thread is for 2.0 discussion on the technical roadmap. Community engagement is not part of this topic. As mentioned above, I shared the same goal and sentiment as you. And I also treat this issue seriously and by no means am dismissing you. But, unless the community can have a proper discussion on this, others have no way of working together with you on this.

@StevenJokes here is how we intended the discussion channels to be used: https://mxnet.apache.org/versions/1.6/community/contribute.html
And here's the code of conduct of this project: http://www.mxnet.incubator.apache.org/foundation/policies/conduct.html
And very much contrary to what you said, I've been on this project for the past three years and I care deeply about having a healthy community, and opinions on making it better like yours.

@qqaatw @StevenJokes I started a thread for this on your behalf here: #18963, hope that's ok.

@sxjscience
This comment was marked as off-topic.
Show comment
@lanking520
Member
lanking520 commented 25 days ago
@StevenJokes Thanks for your effort working on MXNet project and D2L part. It's really an awesome work you have done. We should definitely raise our attention on active contributors. Before we drive this thread into cat-fight, I would recommend you open another issue like Sheng mentioned in the issue. We can discuss over there. This one is just the roadmap for 2.0 features and updates. If you have concerns to MXNet community, please feel free to reach out to dev@mxnet.apache.org. For the no-official reply part, we all just open-source and voluntarily contribute to the community, so there is absolute no gauranteed 3-day respond mechanism. We tried our best to maintain this and we will keep doing that.

If possible, I would recommend to withdraw the extreme comment to this thread and put it to the community conversation channel. Thanks for your support!

@StevenJokes
This comment was marked as off-topic.
Show comment
@ehsanmok
Contributor
ehsanmok commented 25 days ago
@StevenJokes Thanks for your comments! Couple of things:

Your comments are violating the Code of Conduct. Rude and harassing comments, no matter how useful they are, will not be tolerated and listened to. We are a big community here, please be respectful.
Pretty much all of your peers are aware of the forum issues so there is dedicated D2L forum for your specific issues.
@StevenJokes
This comment was marked as off-topic.
Hide comment
@StevenJokes
StevenJokes 25 days ago Contributor
OK. You'd better not listen. I have read Code of Conduct.

@pengzhao-intel
Contributor
pengzhao-intel commented 23 days ago
What's plan of the validation and user tutorial?
Does the example still work?

@szha
Member
Author
szha commented 23 days ago •
What's plan of the validation and user tutorial?

I think the tutorials (in the form of markdown, shown on the website) are currently validated in the website build pipeline. Examples will be maintained in apache/incubator-mxnet-examples with CI enforcement.

@hmf
hmf commented 9 days ago •
@szha Just a small comment and question on the issue of the tutorials asked by @pengzhao-intel. I am starting to look at this framework and find that I need to hunt down the dependencies so that the project examples work.

Case in point the MNIST example has a link to the setup. However, we still need information on the dependencies for the ai.djl.basicdataset.Mnist import. That important information is found here. I have not found a link to this page from the documentation.

I would also like to know how are you validate the tutorials (I haven't checked so they may be in perfect working order).

I am interested in this because I have other projects in Scala (example) wherein I generate a site. In one case I use for example Laika to process the Markdown. To ensure the code is working I use either Tut or Mdoc, which supersedes it to preprocess the Markdown sources. Note that all the code are in the Markdown files and are checked when they are compiled and execute (output can be placed in the source Markdown). Thus code and documentation are always in sink. Is there a way to do this in Java?

EDIT: just realized that the checks above won't catch any missing references to dependencies.

@szha
Member
Author
szha commented 9 days ago
@hmf thanks for pointing out the issue on dependencies.

I would also like to know how are you validate the tutorials (I haven't checked so they may be in perfect working order).

For tutorials on mxnet.apache.org, they are jupyter notebooks in markdown format (processed by notedown) that are executed at the time of building the documentation. for the examples folder, we plan to move them to the new repo gradually, guarded by regular CI checks to make sure they are working.

Since the example issues you pointed out belong to DJL, @lanking520 will likely be of best help in resolving them.

@hmf
hmf commented 8 days ago
@szha Thanks for the answers regarding the checks. Thanks for link also.

Since the example issues you pointed out belong to DJL, @lanking520 will likely be of best help in resolving them.

Oops, my apologies. Scratch that.

@StevenJokes
Write
Preview
You can't perform this action at this time.

Assignees
No one assigned
Labels
RFC
Projects
None yet
Milestone
No milestone
Linked pull requests
Successfully merging a pull request may close this issue.

None yet
Notifications
Customize
You’re not receiving notifications from this thread.
9 participants
@hmf
@szha
@sxjscience
@ehsanmok
@analog-cbarber
@lanking520
@pengzhao-intel
@qqaatw
@StevenJokes
