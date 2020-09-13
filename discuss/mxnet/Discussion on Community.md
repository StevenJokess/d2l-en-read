

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 21:30:57
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 21:31:30
 * @Description:https://github.com/apache/incubator-mxnet/issues/18963
 * @TODO::
 * @Reference:
-->

szha commented 25 days ago
Description
A divergent discussion in #18931 surfaced insufficient support in the discuss forums which is an important issue. @StevenJokes and @qqaatw brought up a valid point that it's vital to the community.

Here I'd like to tap on that discussion and explore how our community can better help new users engage by making sure their inquiries are heard. Topics in this discussion include: what channels to use for different types of discussion, how to surface unanswered questions more easily, how to build mechanisms to have users help each other out.

@szha szha added the RFC label 25 days ago
@szha szha mentioned this issue 25 days ago
[Development] MXNet 2.0 Update #18931
 Open
@pengzhao-intel
Contributor
pengzhao-intel commented 24 days ago •
My 0.02, it will be better to have a unified place to discuss all MXNet related issues. There are multiple forums but I don't think it's active, including dev@, JIRA.

I think GitHub will be a good choice for the interface of MXNet and their user/developers.

@StevenJokes
Contributor
StevenJokes commented 24 days ago •
I don't think GitHub will be the only one place.
Please look the mxnet issues' numbers. Too many.
It's hard to search directly in google too.
Keep only bugs to report in github.

We need a discussion that it's easy to search and solve some specific problems.

Frequent Asked Questions is a good try.
BUT!!
image
404
image

Maybe it is https://mxnet.apache.org/versions/1.6/api#FAQ

--

And you should list
https://lists.apache.org/list.html?dev@mxnet.apache.org
in README.md.
There is no wonder that no one reply to you.
I don't know, and I believe thatmany people don't know the place.

@szha
Why do you tell them to ask in discuss.mxnet.io?
But no reply to them these months.
Being open is not in words, but in action.
Being friendly is not be "nice guy" and polite, but treat their question carefully.

Being a leader is not "open some topics" to let them just make some questions no one will reply , but answer their questions , join their discussions to understand what we need to do next , and invite them to create more interesting things together.

@szha
Member
Author
szha commented 21 days ago
I'm clarifying the communication channel usage in #18992

@petewerner
petewerner commented 9 days ago
What about a discord, perhaps even a channel off an existing ML/DL focused discord.

As a new user I look at the forums and theres pages of questions with no replies, I'm not going to bother posting there.

The slack channel seems more focussed on development discussion and not newb questions which is fine. Also you have to email someone to get access which is a barrier. Not a huge one but friction nonetheless.

There needs to be a benefit for experienced people willing to help, if there was a deep learning discord with other experts it would be worth their time to hang around and offer help in a new user/questions channel, because they would hopefully benefit from the discussion in other parts of the discord.
