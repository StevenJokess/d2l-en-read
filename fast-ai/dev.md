

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-06 23:16:34
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 00:03:26
 * @Description:
 * @TODO::
 * @Reference:https://docs.fast.ai/dev/develop.html
-->

To do an editable install, from inside the cloned fastai directory:

   cd fastai
   pip install -e ".[dev]"

但是添加[dev]会告诉pip在fastai/setup.py中的dev_requirements字典变量的dev组中安装可选包。这些额外的依赖关系只有开发人员和贡献者才需要。

最好不要使用python setup.py开发方法doc。

当你想与主同步你的代码库时，只需回到复制的fastai目录并更新它:

   git pull

你不需要做任何其他的事情。



可编辑的安装说明

如果您刚刚接触可编辑安装，请参考可编辑安装及其示例。

本节将演示可编辑安装如何与fastai一起工作，包括一些需要理解的重要细微差别。

首先，确保您在正确的python环境中(conda激活fastai，或者任何您称为环境的东西，如果您使用的是系统范围安装，那么您不需要激活任何东西，尽管使用专用的虚拟环境来使用fastai要安全得多)。

让我们从卸载fastai开始:

pip   uninstall -y fastai
conda uninstall -y fastai

TODO:
它和pip完全一样，只是通过编辑~/anaconda3/envs/fastai/lib/python3.6/site-packages/conda.pth来执行。

因此，如果conda是您的首选方法，您可能会认为使用这种方法更好。

我们不推荐使用这种方法，因为它不适用于conda的常规安装(正常的conda包安装将在运行时取代可编辑的安装)。与pip不同的是，conda的普通包忽略了它们的可编辑版本，反之亦然——因此您最终只能同时拥有两个可编辑版本，而只有一个可以工作。此外，conda不支持由pip实现的额外依赖项(dev依赖项)。

To uninstall the editable conda version you must use:

cd ~/github/fastai
conda develop -u .

(Ctrl-C to kill jupyter)
您可以安装nb_conda_kernels，它为每个conda环境提供一个单独的jupyter内核，以及用于处理设置的适当代码。这使得切换conda环境就像切换jupyter内核一样简单(例如，从内核菜单中切换)。你不需要担心你从哪个环境开始木星笔记本-只要选择正确的环境从笔记本。

---

如何安全有效地使用CLI在git repo中搜索/替换文件。操作时不能触及。git下的任何东西:

find . -type d -name ".git" -prune -o -type f -exec perl -pi -e 's|OLDSTR|NEWSTR|g' {} \;


但它触摸(1)es所有文件减慢git侧，所以我们想做的文件，实际上包含旧模式:

grep --exclude-dir=.git -lIr "OLDSTR" . | xargs -n1 perl -pi -e 's|OLDSTR|NEWSTR|g'
