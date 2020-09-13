

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 20:27:54
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 20:28:03
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_attention-mechanisms/attention.html
 * @TODO::
 * @Reference:
-->
7 replies
14 Jul
Van_​​Tran
For the batched dot product I don’t understand why we divide by sqrt(d) instead of d. In my eyes d perfectly takes out the problem of higher dimensions blowing up the dot product and the square root adds needless complexity. However, the first intuition is to use d, so there must be a reason for the sqrt. What am I missing here?

1 reply
14 Jul▶ Van_Tran
goldpiggy
Hi @Van_Tran, great question! Please refer to the original paper section 3.2.1:
image
The reason we don’t use d is similar, a large d may lead to extremely small gradients.

1 reply
26 Jul▶ goldpiggy
pyzeus
It is really useful. Will there be tensorflow implementation for the remaining topics?.

1 reply
27 Jul▶ pyzeus
goldpiggy
Hi @pyzeus, thanks! Yeah we are writing the TF version now!

1 reply
27 Jul
Richard
Is this correct in PyTorch MLPAttention?

query, key = self.W_k(query), self.W_q(key)
I think it should be

query, key = self.W_q(query), self.W_k(key)
1 reply
28 Jul▶ goldpiggy
pyzeus
Thank you so much for the effort!

28 Jul▶ Richard
goldpiggy
Great call @Richard ! Will fix and test it!

Continue Discussion
