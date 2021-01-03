https://github.com/iamhankai/cpp-pytorch

LOADING YOUR SCRIPT MODULE IN C++ and EXECUTING

1. Download LibTorch here and unzip

2. Cmake

```
mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH=/Users/hankai/code/cpp-pytorch/libtorch ..
make
```
Run demo

./example-app ../model.pt ../dog.png ../synset_words.txt

Input image and predicted label: n02108422 bull mastiff, bingo!
