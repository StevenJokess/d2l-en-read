

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 18:36:21
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-06 19:06:53
 * @Description:
 * @TODO::
 * @Reference:https://learning.oreilly.com/library/view/introducing-mlops/9781492083283/
 * https://learning.oreilly.com/library/view/agile-ai/9781492074984/ch03.html#model_integration_and_deployment
 * https://learning.oreilly.com/library/view/introducing-mlops/9781492083283/ch09.html#deploy_to_production
-->
目前组织创建的分析和机器学习(ML)模型中，有一半以上从未投入生产。运作化的一些挑战和障碍是技术上的，但其他的是组织上的。不管怎样，底线是没有生产的模型不能提供业务影响。

这本书介绍了MLOps的关键概念，以帮助数据科学家和应用工程师不仅操作ML模型来驱动真正的业务变化，而且还随着时间的推移维护和改进这些模型。通过基于世界各地大量MLOps应用程序的课程，9位机器学习专家对模型生命周期的5个步骤(构建、预生产、部署、监视和治理)提供了深刻见解，揭示了如何在整个过程中注入健壮的MLOps流程。

这本书可以帮助你:

通过减少整个ML管道和工作流的摩擦，实现数据科学价值

通过再培训、定期调整和完全重塑来完善ML模型，以确保长期的准确性

将MLOps生命周期设计为使用无偏见、公平和可解释的模型来最小化组织风险

为管道部署和更复杂、更不标准化的外部业务系统操作ML模型

---

模型集成和部署

在生产环境中部署模型是作为一个单独的领域出现的:MLOps。只有在模型开始与实时客户数据交互之后，生产中才会出现许多问题。例如，如果一个模型的精确度突然上升，这可能是一件非常糟糕的事情，可能意味着异常值或模型漂移。安全性、隐私性、偏见、伦理和日益增长的各种遵从性问题都在模型部署的这一点上出现。这些当前的操作问题与IT操作人员以前必须处理的问题有很大的不同。

为了建立对人工智能代表你的企业所做决策的信任，你需要一个合适的模型管理策略。这意味着定期刷新模型，监控预测的准确性，以及其他反馈循环，比如解释模型决策的能力。模型信任在受监管的行业中尤为重要，它能确保自动决策不带有偏见，并恰当地代表你的品牌。

---

部署到生产环境

在典型的大型金融服务组织中，生产环境不仅与设计环境分离，而且可能基于不同的技术堆栈。用于关键操作的技术堆栈——比如交易验证，但也可能是贷款验证——总是发展缓慢。

历史上，生产环境主要支持规则和线性模型，比如logistic回归。有些可以处理更复杂的模型，如PMML或JAR文件。对于不那么关键的用例，Docker部署或通过集成的数据科学和机器学习平台进行部署是可能的。因此，模型的操作化可能涉及从单击按钮到基于Microsoft Word文档编写公式的各种操作。

在这样一个高价值用例中，部署模型的活动日志对于监视模型性能至关重要。根据监视的频率，反馈回路可能是自动化的，也可能不是。例如，如果任务一年只执行一次或两次，并且大部分时间花在询问数据问题上，那么自动化可能是不必要的。另一方面，如果评估是每周完成的，自动化可能是必要的，这可能是持续几个月的短期贷款的情况。

---

https://learning.oreilly.com/library/view/machine-learning-systems/9781617293337/kindle_split_021.html

DEPLOYING
At this point, you may feel confident about your models based on the guarantees that the validations in the build pipeline give you. You could potentially move forward with deployment. In this context, deployment means to publish the component of your machine learning system and start acting on real user requests, as we explored in chapter 8. For your JJB team, the component system in this step looks something like figure 9.3.

Figure 9.3. Model deployment


After tests have passed, the application JAR is pushed to a remote artifact repository. Then the build pipeline calls the application-serving platform’s API to start the deployment of the application. The serving platform will need to provision the necessary resources, download the JAR to a sandbox, and then start the application.

How often should you deploy the system? What determines that you should do a deploy? This is actually a very complicated topic. Roughly speaking, there are four approaches to when you deploy and why, as shown in table 9.2.

Table 9.2. Approaches to deployments
Style

Criteria

Frequency

Advantages

Disadvantages

Ad hoc	None	Variable, but often infrequent	Simple and flexible	Deploys can be difficult due to low deployment skills and/or automation
At milestones	Achieving some meaningful development milestone	Weeks to months	Clarifies planning around deploys	Unplanned deploys can be hard
Periodically	Reaching a determined amount of time	Days to weeks	Regularity builds skills and speed	Can be labor intensive
Continuously	Committing to the master branch	Multiple times per day	Fast responses to change	Requires investment in predeploy enabling capabilities
As you can see, there are some complex trade-offs to consider when deciding how to structure your deployment process. The Jungle Juice Box team chooses a continuous deployment process, after using other processes earlier in the company’s history. In their experimentations with variations on the approaches in table 9.2, they found that less-frequent deploys led them to underinvest in their build-and-deploy infrastructure. They didn’t deploy that often, and when they did, it was so painful that they wanted to work on anything else, once the deploy was done, instead of improving the deploy process. When they decided that they needed to ship updates to the fruit-recommendation system more quickly, they realized they needed to implement the capabilities that would allow them to continuously deploy their system.

At a base level, they need reliable tests that will tell them whether their application can be deployed. Those tests need to be used by an automated build pipeline capable of determining whether the application should be deployed and then proceeding with that deployment.

They wind up with a flow that looks like figure 9.4, where a series of automated decisions are made to ensure that a given deployment is safe. Note that the predictive system’s capability is tested at two levels. First, unit tests verify properties of the system that can be assessed without using much data. Then, after a deployable version of the application has been built, that release candidate is evaluated on a larger set of data. In this step, metrics about the system’s performance are assessed to ensure that the system as a whole can do a sufficiently good job of its core mission: predicting subscribers’ fruit preferences. This particular technique is sometimes called a metrics-based deploy. Only when both levels of testing have been passed do you call the command to start the application.


---
https://learning.oreilly.com/library/view/practical-automated-machine/9781492055587/ch09.html#model_deployment_and_inferencing

模型部署和推断

当您对模型感到满意时，单击模型性能报告中的“应用模型”选项(如图9-33所示)。这将带您完成一个简单而直观的流程，选择一个测试数据集/实体，并将列添加到其中，这些列将根据这个训练过的模型进行填充。当新的数据记录进入这个数据流实体时，新添加的列将被自动填充，从而推断我们刚刚构建和部署的模型。
