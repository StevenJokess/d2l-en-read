

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 17:23:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-17 17:24:21
 * @Description:
 * @TODO::
 * @Reference:
 * [1]: https://github.com/udacity/deep-learning-v2-pytorch/blob/master/project-tv-script-generation/helper.py
 * [2]: https://blog.csdn.net/weixin_44791964/article/details/102851214
-->

```
import os
import pickle

SPECIAL_WORDS = {'PADDING': '<PAD>'}

def preprocess_and_save_data(dataset_path, token_lookup, create_lookup_tables):
    """
    Preprocess Text Data
    """
    text = load_data(dataset_path)

    # Ignore notice, since we don't use it for analysing the data
    text = text[81:]

    token_dict = token_lookup()
    for key, token in token_dict.items():
        text = text.replace(key, ' {} '.format(token))

    text = text.lower()
    text = text.split()

    vocab_to_int, int_to_vocab = create_lookup_tables(text + list(SPECIAL_WORDS.values()))
    int_text = [vocab_to_int[word] for word in text]
    pickle.dump((int_text, vocab_to_int, int_to_vocab, token_dict), open('preprocess.p', 'wb'))
```

---
[2]
def preprocess_input(x):
    x /= 255.
    x -= 0.5
    x *= 2.
    return x
