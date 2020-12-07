

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 19:31:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 17:54:34
 * @Description:
 * @TODO::
 * @Reference:https://learning.oreilly.com/library/view/programming-pytorch-for/9781492045342/ch09.html#idm45762347307368
-->

Generating Text with GPT-2
Like BERT, the official GPT-2 release from OpenAI is a TensorFlow model. Also like BERT, Hugging Face has released a PyTorch version that is contained within the same library (pytorch-transformers). However, a burgeoning ecosystem has been built around the original TensorFlow model that just doesn’t exist currently around the PyTorch version. So just this once, we’re going to cheat: we’re going to use some of the TensorFlow-based libraries to fine-tune the GPT-2 model, and then export the weights and import them into the PyTorch version of the model. To save us from too much setup, we also do all the TensorFlow operations in a Colab notebook! Let’s get started.

Open a new Google Colab notebook and install the library that we’re using, Max Woolf’s gpt-2-simple, which wraps up GPT-2 fine-tuning in a single package. Install it by adding this into a cell:

!pip3 install gpt-2-simple
Next up, you need some text. In this example, I’m using a public domain text of PG Wodehouse’s My Man Jeeves. I’m also not going to do any further processing on the text after downloading it from the Project Gutenberg website with wget:

!wget http://www.gutenberg.org/cache/epub/8164/pg8164.txt
Now we can use the library to train. First, make sure your notebook is connected to a GPU (look in Runtime→Change Runtime Type), and then run this code in a cell:

import gpt_2_simple as gpt2

gpt2.download_gpt2(model_name="117M")

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              "pg8164.txt",model_name="117M",
              steps=1000)
Replace the text file with whatever text file you’re using. As the model trains, it will spit out a sample every hundred steps. In my case, it was interesting to see it turn from spitting out vaguely Shakespearian play scripts to something that ended up approaching Wodehouse prose. This will likely take an hour or two to train for 1,000 epochs, so go off and do something more interesting instead while the cloud’s GPUs are whirring away.

Once it has finished, we need to get the weights out of Colab and into your Google Drive account so you can download them to wherever you’re running PyTorch from:

gpt2.copy_checkpoint_to_gdrive()
That will point you to open a new web page to copy an authentication code into the notebook. Do that, and the weights will be tarred up and saved to your Google Drive as run1.tar.gz.

Now, on the instance or notebook where you’re running PyTorch, download that tarfile and extract it. We need to rename a couple of files to make these weights compatible with the Hugging Face reimplementation of GPT-2:

mv encoder.json vocab.json
mv vocab.bpe merges.txt
We now need to convert the saved TensorFlow weights into ones that are compatible with PyTorch. Handily, the pytorch-transformers repo comes with a script to do that:

 python [REPO_DIR]/pytorch_transformers/convert_gpt2_checkpoint_to_pytorch.py
 --gpt2_checkpoint_path [SAVED_TENSORFLOW_MODEL_DIR]
 --pytorch_dump_folder_path [SAVED_TENSORFLOW_MODEL_DIR]
Creating a new instance of the GPT-2 model can then be performed in code like this:

from pytorch_transformers import GPT2LMHeadModel

model = GPT2LMHeadModel.from_pretrained([SAVED_TENSORFLOW_MODEL_DIR])
Or, just to play around with the model, you can use the run_gpt2.py script to get a prompt where you enter text and get generated samples back from the PyTorch-based model:

python [REPO_DIR]/pytorch-transformers/examples/run_gpt2.py
--model_name_or_path [SAVED_TENSORFLOW_MODEL_DIR]
Training GPT-2 is likely to become easier in the coming months as Hugging Face incorporates a consistent API for all the models in its repo, but the TensorFlow method is the easiest to get started with right now.

BERT and GPT-2 are the most popular names in text-based learning right now, but before we wrap up, we cover the dark horse of the current state-of-the-art models: ULMFiT.

---

And as for GPT-2, if you’re after generated text, then yes, it’s a better fit, but for classification purposes, it’s going to be harder to approach ULMFiT or BERT performance. One thing that I do think might be interesting is to let GPT-2 loose on data augmentation; if you have a dataset like Sentiment140, which we’ve been using throughout this book, why not fine-tune a GPT-2 model on that input and use it to generate more data?

GPT-2则终于释出完整版，开源15亿参数模型。[2]
https://openai.com/blog/gpt-2-1-5b-release/


[2]: 2019 年过去了，人工智能领域干了些什么？ - 量子位的回答 - 知乎
https://www.zhihu.com/question/365135309/answer/999770457
