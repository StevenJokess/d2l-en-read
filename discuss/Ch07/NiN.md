

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-13 20:38:05
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-09-13 20:38:31
 * @Description:http://preview.d2l.ai/d2l-en/master/chapter_convolutional-modern/nin.html
 * @TODO::
 * @Reference:
-->
2 replies
25 Aug
Nish
Am I correct in thinking that there is some implicit rounding down of dimensions going on when the integer division by the stride would leave a remainder?

The base formula for the width of the output representation of a convolution layer is given by (width_of_input - filter_size + 2*padding) / stride + 1

Taking the first NiN block as an example, the input is a 224x224 large image. This layer has a 11x11 kernel with stride of 4, and padding explicitly set to 0 (the 1x1 conv layers shouldn’t change the dimension so I ignore them here). The above formula gives (224 - 11)/4 + 1 as the output dimension, which would give 54.25 - I see the output shape from the dimensions test in the textbook chapter is 54.

The same thing happens for many other layers in the network - an imperfect division by a stride. When this happens, does PyTorch implicitly crop some columns from the left/right/top/bottom at random to make it round down?

Unrelatedly, here are my calculations for the resource usage of the NiN in the textbook chapter:

INPUT: 224 x 224 x 1	ACTIVS: 224 * 224		PARAMS: 0
CONV(1,96,11,4,0)		ACTIVS: 96 * 54 * 54	PARAMS: (11*11*1)*96
CONV(96,96,1,1,0)		ACTIVS: 96 * 54 * 54	PARAMS: (1*1*96)*96
CONV(96,96,1,1,0)		ACTIVS: 96 * 54 * 54	PARAMS: (1*1*96)*96
MaxPool(3,2)			ACTIVS: 96 * 26 * 26      PARAMS: 0
NiNBlock(96,256,5,1,2)	ACTIVS: 3*(256 * 26 * 26)   PARAMS: 256 * (256+256+(5*5*96))
MaxPool(3,2)			ACTIVS: 256 * 12 * 12	PARAMS: 0
NiNBlock(256,384,3,1,1)	ACTIVS: 3*(384 * 12 * 12)	PARAMS: 384 * (384+384+(3*3*256))
MaxPool(3,2)			ACTIVS:	384 * 5 * 5		PARAMS: 0
Dropout				ACTIVS: 384 * 5 * 5		PARAMS: 0
NiNBlock(384,10,3,1,1)	ACTIVS: 3*(10 * 5 * 5)		PARAMS: 10 * (10+10+(3*3*384))
AdaptiveMaxPool		ACTIVS: 10				PARAMS: 0
Flatten				ACTIVS: 10				PARAMS: 0
When training: we need 2 * the ACTIVS sum (values + gradients), and 3 * the PARAMS sum (values, gradients, and a cache for momentum/Adam)

When testing: we just need the sum of activs + params. If we’re being clever we can erase previous ACTIVS as we go, so we only need the sum of the largest two consecutive ACTIVS. We also don’t need the Dropout ACTIVS.

1 reply
27 Aug
goldpiggy
 Nish:
When this happens, does PyTorch implicitly crop some columns from the left/right/top/bottom at random to make it round down?

Hey @Nish, great question. I am not exactly sure which edge does PyTorch choose to round down. However, if you use some level of padding, it won’t lose any information since you just remove that edge’s padding away.

Continue Discussion
