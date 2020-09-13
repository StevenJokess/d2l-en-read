

<!--
 * @version:
 * @Author:  StevenJokes https://github.com/StevenJokes
 * @Date: 2020-09-13 19:34:36
 * @LastEditors:  StevenJokes https://github.com/StevenJokes
 * @LastEditTime: 2020-09-13 19:37:06
 * @Description:
 * @TODO::
 * @Reference:
-->

Continue Discussion
21 replies
4 Jun
S_​X
@mli Between MXNET and Pytorch, which would you recommend to use for a beginner in deep learning? Is either of them fine?

3 replies
4 Jun▶ S_X
Kv​Kid
Further to this, since tensorflow is “49% faster” than MXNet, why have you decided to include MXNET and Pytorch instead of tensorflow api?

*I am new at deep learning and commend the thorough guide!

1 reply
4 Jun▶ S_X
mli
You could compare the MXNet/PyTorch code tabs and choose the one you like. I personally like more MXNet as I’m one of its creator, but PyTorch is more popular. From the learning aspect, I think any framework is fine, it’s a just tool for you to understand and try deep learning algorithms.

1 reply
4 Jun▶ KvKid
mli
I think “Tensorflow is 49% faster than MXNet” is not general true. But we do plan to add TensorFlow implementations.

5 Jun▶ S_X
Elie_​G
I have not used MXNET but in my view You should consider learning pytorch. It has big support and big community around it. You will find that it is easier to learn a framework that is widely adopted since you can get support from everywhere. Beside that, recruiters are likely to make it a requirement to know pytorch or tensorflow.

5 Jun
Bashar_​​Fadil
Hi, thank you for putting this course together. I had a question about gpu/cpu. I have AMD 3950x Ryzen processor and an AMD Vega Frontier GPU. Which one do you recommend I use? Does it matter? If GPU, is installation much different than NVidia? Does having multiple GPUs make a difference ( I have two Vega frontier GPUs)?

1 reply
5 Jun▶ Bashar_Fadil
mli
Unfortunately AMD GPUs are not well supported by deep learning frameworks right now. I suggest you to have a Nvidia GPU.

6 Jun▶ mli
S_​X
@mli thanks for the answer!

12 Jun
JimK
Help! I’m using the Jetson Nano. I’m having trouble installing either Miniconda or Archiconda. Can someone please help me get Anaconda installed on the Nano. Thanks!

16 Jun
duke
I was able to complete everything in the Installation chapter of the book except

pip install mxnet-cu90==1.6.0

The response I’m getting is

“Collecting mxnet-cu90==1.6.0
Could not find a version that satisfies the requirement mxnet-cu90==1.6.0 (from versions: )
No matching distribution found for mxnet-cu90==1.6.0”

I’ve tried several variations and no progress with anything to do with MXNet. I’m running on macos 10.12, and CUDA Release 9.0 V9.0.175 (the latest version for that OS).

Any suggestions? TIA

1 reply
18 Jun▶ duke
duke
Based on what I’m finding from my own digging into this problem, it’s looking like the book is assuming that readers are developing on non-macOS platforms without saying so. According to https://mxnet.apache.org/get_started/?version=v1.6.0&platform=macos&language=python&processor=gpu&environ=pip
There is no “pip” install option for macOS. It seems that MXNet will have to be manually built from source code on individual macOS devices, which is much more involved.

2 Jul
skywalker_​H
There is no mxnet110 developed yet(most recently 10*), while the link “CUBA” in the paragraph will lead to the downloading page of CUBA 11.0 . It is contradictary, so is mxnet100 compatable with CUBA 11.0??

2 replies
2 Jul▶ skywalker_H
skywalker_​H
@mli :heart:heart:heart:heart:heart:heart:heart:heart:heart:heart:heart:heart:heart:heart:heart:heart:heart:

3 Jul▶ skywalker_H
goldpiggy
Hi @skywalker_H, CUDA upgrades the version regularly, you should be able to use CUDA10.1. http://d2l.ai/chapter_appendix-tools-for-deep-learning/aws.html#installing-cuda

1 Aug
Powerpig
I am using a Surface notebook with Intel Graphics chips, does it mean that I’d better get a new computer with NVidia cards?

1 reply
3 Aug▶ Powerpig
goldpiggy
Hey @Powerpig, you are welcome to use any GPU. More info can be found in this appendix. :slight_smile:

6 Aug
Steven​Jokes
Recommend my post: Do these before you ask
mxnet installation is frastruating.
1st-3th Try:
(mxnet) C:\Users\a8679>pip install mxnet==1.6.0
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting mxnet==1.6.0
Downloading https://pypi.tuna.tsinghua.edu.cn/packages/6c/3c/c800c23068ef23dedbb2641574b24cbc6d51c7d7b7bddbc803a93d7409d3/mxnet-1.6.0-py2.py3-none-win_amd64.whl (26.9 MB)
|████████████████████████████████| 26.8 MB 18 kB/s eta 0:00:05ERROR: Exception:
Traceback (most recent call last):
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_vendor\urllib3\response.py”, line 425, in _error_catcher
yield
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_vendor\urllib3\response.py”, line 507, in read
data = self._fp.read(amt) if not fp_closed else b""
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_vendor\cachecontrol\filewrapper.py”, line 62, in read
data = self.__fp.read(amt)
File “C:\Users\a8679\anaconda3\lib\http\client.py”, line 457, in read
n = self.readinto(b)
File “C:\Users\a8679\anaconda3\lib\http\client.py”, line 501, in readinto
n = self.fp.readinto(b)
File “C:\Users\a8679\anaconda3\lib\socket.py”, line 589, in readinto
return self._sock.recv_into(b)
File “C:\Users\a8679\anaconda3\lib\ssl.py”, line 1071, in recv_into
return self.read(nbytes, buffer)
File “C:\Users\a8679\anaconda3\lib\ssl.py”, line 929, in read
return self._sslobj.read(len, buffer)
socket.timeout: The read operation timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\cli\base_command.py”, line 186, in _main
status = self.run(options, args)
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\commands\install.py”, line 331, in run
resolver.resolve(requirement_set)
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\legacy_resolve.py”, line 177, in resolve
discovered_reqs.extend(self._resolve_one(requirement_set, req))
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\legacy_resolve.py”, line 333, in _resolve_one
abstract_dist = self._get_abstract_dist_for(req_to_install)
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\legacy_resolve.py”, line 282, in _get_abstract_dist_for
abstract_dist = self.preparer.prepare_linked_requirement(req)
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\operations\prepare.py”, line 482, in prepare_linked_requirement
hashes=hashes,
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\operations\prepare.py”, line 287, in unpack_url
hashes=hashes,
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\operations\prepare.py”, line 159, in unpack_http_url
link, downloader, temp_dir.path, hashes
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\operations\prepare.py”, line 303, in _download_http_url
for chunk in download.chunks:
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\utils\ui.py”, line 160, in iter
for x in it:
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_internal\network\utils.py”, line 39, in response_chunks
decode_content=False,
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_vendor\urllib3\response.py”, line 564, in stream
data = self.read(amt=amt, decode_content=decode_content)
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_vendor\urllib3\response.py”, line 529, in read
raise IncompleteRead(self._fp_bytes_read, self.length_remaining)
File “C:\Users\a8679\anaconda3\lib\contextlib.py”, line 130, in exit
self.gen.throw(type, value, traceback)
File “C:\Users\a8679\anaconda3\lib\site-packages\pip_vendor\urllib3\response.py”, line 430, in _error_catcher
raise ReadTimeoutError(self._pool, None, “Read timed out.”)
pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host=‘pypi.tuna.tsinghua.edu.cn’, port=443): Read timed out.

4th try:

(mxnet) C:\Users\a8679>pip install mxnet==1.6.0
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Collecting mxnet==1.6.0
Downloading https://pypi.tuna.tsinghua.edu.cn/packages/6c/3c/c800c23068ef23dedbb2641574b24cbc6d51c7d7b7bddbc803a93d7409d3/mxnet-1.6.0-py2.py3-none-win_amd64.whl (26.9 MB)
|████████████████████████████████| 26.9 MB 297 kB/s
Collecting requests<2.19.0,>=2.18.4
Downloading https://pypi.tuna.tsinghua.edu.cn/packages/49/df/50aa1999ab9bde74656c2919d9c0c085fd2b3775fd3eca826012bef76d8c/requests-2.18.4-py2.py3-none-any.whl (88 kB)
|████████████████████████████████| 88 kB 4.1 MB/s
Collecting graphviz<0.9.0,>=0.8.1
Downloading https://pypi.tuna.tsinghua.edu.cn/packages/53/39/4ab213673844e0c004bed8a0781a0721a3f6bb23eb8854ee75c236428892/graphviz-0.8.4-py2.py3-none-any.whl (16 kB)
ERROR: Could not find a version that satisfies the requirement numpy<1.17.0,>=1.8.2 (from mxnet==1.6.0) (from versions: none)
ERROR: No matching distribution found for numpy<1.17.0,>=1.8.2 (from mxnet==1.6.0)

5th try:
Requirement already satisfied: certifi>=2017.4.17 in c:\users\a8679\anaconda3\lib\site-packages (from requests<2.19.0,>=2.18.4->mxnet==1.6.0) (2019.11.28)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in c:\users\a8679\anaconda3\lib\site-packages (from requests<2.19.0,>=2.18.4->mxnet==1.6.0) (3.0.4)
ERROR: botocore 1.17.20 has requirement docutils<0.16,>=0.10, but you’ll have docutils 0.16 which is incompatible.
ERROR: awscli 1.18.97 has requirement docutils<0.16,>=0.10, but you’ll have docutils 0.16 which is incompatible.
Installing collected packages: idna, urllib3, requests, numpy, graphviz, mxnet
Attempting uninstall: idna
Found existing installation: idna 2.8
Uninstalling idna-2.8:
Successfully uninstalled idna-2.8
Attempting uninstall: urllib3
Found existing installation: urllib3 1.25.8
Uninstalling urllib3-1.25.8:
Successfully uninstalled urllib3-1.25.8
Attempting uninstall: requests
Found existing installation: requests 2.22.0
Uninstalling requests-2.22.0:
Successfully uninstalled requests-2.22.0
Attempting uninstall: numpy
Found existing installation: numpy 1.18.1
Uninstalling numpy-1.18.1:
Successfully uninstalled numpy-1.18.1
Successfully installed graphviz-0.8.4 idna-2.6 mxnet-1.6.0 numpy-1.16.6 requests-2.18.4 urllib3-1.22

# install assignment dependencies.
# since the virtual env is activated,
# this pip is associated with the
# python binary of the environment
pip install -r requirements.txt
6 Aug
Ali_​coder
I have geforce mx250 graphics. I dont think i have cuda support. What platform should i run the code.

2 replies
6 Aug▶ Ali_coder
goldpiggy
Hey @Ali_coder, please see appendix for more info.

7 Aug
Steven​Jokes
@Ali_coder
Recommend my post: Do these before you ask

You can try to google it before you ask. I’m a AMD user, but all Nvidia GPU support cuda in my mind.

If you use mxnet, go to https://mxnet.apache.org/versions/1.6/get_started/
image
image
You can use CPU version or CUDA version in your computer.
Or just use a server image
image
image

Or just google it:
Can I use MX 250 Graphic Card for basic Deep Learning ?
image
Then go to the nvidia website:
image

image
But you can’t find the CUDA download…
So you just search it, then you find mxnet doesn’t support cuda11 yet.
image

 NVIDIA Developer – 6 Oct 15

CUDA Toolkit 11.0 Update 1 Downloads
Select Target Platform Click on the green buttons that describe your target platform. Only supported platforms will be shown. By downloading and using the software, you agree to fully comply with the terms and conditions of the CUDA EULA. Operating...

So you search for

image
You can select the right Platform for your cuda:
image
http://preview.d2l.ai/d2l-en/master/chapter_appendix-tools-for-deep-learning/aws.html#Installing%20CUDA

After you installed cuda 10.2 , you can install mxnet:
Example:
image
Give you an exercise:

use google to install pytorch-gpu locally
22 Aug
Steven​Jokes
stackoverflow.com
Josiah Yoder
How do I install the d2l library on Windows without conda?
python, pip, pytorch, d2l
asked by Josiah Yoder on 05:23PM - 22 Jul 20 UTC
Ha, I found an cute user. If you are Josiah Yoder, please tell me it’s ok to publish it

Continue Discussion

https://discuss.d2l.ai/uploads/default/original/1X/20bc2d5f6e2ebde836af05217ce98908ee73693a.png


https://discuss.d2l.ai/uploads/default/original/1X/ea7a5fbb380e19bc09ccfd60bb8a7e16ae120cc5.png

https://discuss.d2l.ai/uploads/default/original/1X/5ab998d553d9d516be9def3ee61ef0da6ad5f480.png

https://discuss.d2l.ai/uploads/default/original/1X/c2889081359bcea6fecd00666ef80eb60d4e8b7f.png

https://discuss.d2l.ai/uploads/default/original/1X/f8e7d6cd68b065c1a63295832d42fb900d9f6887.png

https://discuss.d2l.ai/uploads/default/original/1X/f31957a7af1613ea057e5ceab3e70d3cc7f1c973.png

https://discuss.d2l.ai/uploads/default/original/1X/f31957a7af1613ea057e5ceab3e70d3cc7f1c973.png

https://developer.nvidia.com/cuda-downloads

https://discuss.d2l.ai/uploads/default/optimized/1X/afeb81943f082a2191aab24cf003520a05791719_2_1035x259.png

https://discuss.d2l.ai/uploads/default/original/1X/afeb81943f082a2191aab24cf003520a05791719.png

https://discuss.d2l.ai/uploads/default/original/1X/6c24ae8d640c4748f61e81015180318760d60e3b.png

https://discuss.d2l.ai/uploads/default/optimized/1X/721cb5d77f4781c5e4b589399a516aa56186dcd4_2_1035x711.png

https://stackoverflow.com/questions/63039866/how-do-i-install-the-d2l-library-on-windows-without-conda
