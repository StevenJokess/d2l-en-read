

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-12 22:50:18
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 21:04:57
 * @Description:
 * @TODO::
 * @Reference:https://github.com/pytorch/pytorch#adjust-build-options-optional
 * https://github.com/liueo/TVM-deploy
 * https://nlp.gluon.ai/website/git.html
-->
Get the PyTorch Source
git clone --recursive https://github.com/pytorch/pytorch
cd pytorch
# if you are updating an existing checkout
git submodule sync
git submodule update --init --recursive

Always use git clone --recursive, if not, we can update tvm submodule git submodule update --recursive --init.

---

How to combine multiple commits into one
Sometimes we want to combine multiple commits, especially when later commits are only fixes to previous ones, to create a PR with set of meaningful commits. You can do it by following steps. - Before doing so, configure the default editor of git if you haven’t done so before.

git config core.editor the-editor-you-like
Assume we want to merge last 3 commits, type the following commands

git rebase -i HEAD~3
It will pop up an text editor. Set the first commit as pick, and change later ones to squash.

After you saved the file, it will pop up another text editor to ask you modify the combined commit message.

Push the changes to your fork, you need to force push.

git push --force
