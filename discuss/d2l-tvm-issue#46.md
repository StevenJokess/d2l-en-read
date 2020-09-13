

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 19:16:15
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 19:18:09
 * @Description:https://github.com/d2l-ai/d2l-tvm/issues/46
 * @TODO::
 * @Reference:
-->

colab's python 3.6 doesn't support `pip install`

image
https://user-images.githubusercontent.com/25657787/90603696-3d1e7280-e22e-11ea-8d5e-394e1c276013.png
And tvm py36 is denied.

@StevenJokes
Contributor
Author
StevenJokes commented 25 days ago
Please test and find some solutions.

@StevenJokes
Contributor
Author
StevenJokes commented 21 days ago •
image
I use
!pip install https://haichen-tvm.s3-us-west-2.amazonaws.com/tvm_cu100-0.6.dev0-cp36-cp36m-linux_x86_64.whl
to replace now, but fix
!pip install https://tvm-repo.s3-us-west-2.amazonaws.com/tvm-0.7.dev1-cp37-cp37m-linux_x86_64.whl
ASAP.
https://github.com/bryanyzhu/Video-Tutorial-CVPR2020/blob/master/06_deploy/TVMInference.ipynb

@StevenJokes
Contributor
Author
StevenJokes commented 21 days ago
https://user-images.githubusercontent.com/25657787/90976082-bd194500-e56c-11ea-8ef2-30bbf2ad870d.png

!pip install https://haichen-tvm.s3-us-west-2.amazonaws.com/topi-0.6.dev0-py3-none-any.whl
to replace
!pip install https://tvm-repo.s3-us-west-2.amazonaws.com/topi-0.7.dev1-py3-none-any.whl

image

@StevenJokes
Contributor
Author
StevenJokes commented 21 days ago •
Then I found https://colab.research.google.com/github/uwsampl/tutorial/blob/master/notebook/01_TVM_Tutorial_Intro.ipynb#scrollTo=I7TdPtnqaOuJ
It is really helpful!
https://github.com/uwsampl/tutorial/tree/master/notebook
https://user-images.githubusercontent.com/25657787/90976516-6b72b980-e570-11ea-87d2-533ad0e85fe6.png

@StevenJokes
Contributor
Author
StevenJokes commented 21 days ago •
image
https://user-images.githubusercontent.com/25657787/90979617-dd56fd00-e588-11ea-9867-408d844734c5.png
I've installed llvm why import tvm failed.
https://colab.research.google.com/drive/1AGlPjTZWgZszchJhW41hDWKklr3EEGR8?usp=sharing
