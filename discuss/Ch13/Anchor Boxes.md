

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 20:14:43
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 20:14:50
 * @Description:
 * @TODO::
 * @Reference:
-->
4 replies
7 Aug
Wolf_​​Rage
Can anyone plz explain this statement more…

Therefore, we are usually only interested in a combination containing s1 or r1 sizes and aspect ratios, that is

And this…

That is, the number of anchor boxes centered on the same pixel is n+m−1

Thanks for your time.

1 reply
7 Aug
goldpiggy
Hey @Wolf_Rage, great question!

Therefore, we are usually only interested in a combination containing s1 or r1 sizes and aspect ratios, that is

It can be interpreted as

Therefore, we only cross combine size s1 with all the ratios {r1, r2, …r_m}, and cross combine ratio r1 with all the sizes {s1, s2, …s_n}, this is (𝑠1,𝑟1),(𝑠1,𝑟2),…,(𝑠1,𝑟𝑚),(𝑠2,𝑟1),(𝑠3,𝑟1),…,(𝑠𝑛,𝑟1).

Hence, we has n+m-1 combinations in total. Does it make sense to you now?

1 reply
17 Aug
dayekuaipao
Hello, I have questions about the way that labeling anchors. It seems we need a loop to generate labels in the step as Figure 13.4.2 shows, and it might be slow. I find one other way to generate labels, it’s just find the largest iou and check if it’s larger than threshold.What’s the difference between the two ways?

23 Aug▶ goldpiggy
Wolf_​​Rage
Yes, now it totally makes sense. Thanks a lot.

Continue Discussion
