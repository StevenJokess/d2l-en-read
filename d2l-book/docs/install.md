

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-09-27 19:00:42
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-28 02:21:36
 * @Description:
 * @TODO::
 * @Reference:https://book.d2l.ai/install.html
-->

# 安装

d2lbook包在macOS和Linux下进行测试。(欢迎您贡献一个Windows版本)。

首先确保你有可用的[pip](https://pip.pypa.io/en/stable/)。在选项中，我们建议对pip不支持的库使用[conda](https://docs.conda.io/en/latest/miniconda.html)。

现在安装命令行界面。

```bash
pip install https://github.com/d2l-ai/d2l-book
```


这是一个[d2lbook pip包](https://pypi.org/project/d2lbook/)，但是我们建议您直接在Github上安装最新版本，因为它正在快速开发中。

要构建HTML结果，我们需要[pandoc](https://pandoc.org/)。你可以通过`conda install pandoc`来安装它。

构建PDF版本需要[LibRsvg](https://wiki.gnome.org/Projects/LibRsvg)转换你的SVG图像(我们推荐的格式)，例如`conda install LibRsvg`，当然，你需要有一个LaTeX发行版，例如[Tex Live](https://www.tug.org/texlive/)
apt-get install texlive -y
!apt-get install -y latexmk
!apt-get install -y texlive-xetex

apt update && apt dist-upgrade -y && DEBIAN_FRONTEND=noninteractive apt install -y python3-pip pandoc librsvg2-bin git latexmk texlive-xetex texlive-fonts-extra && apt clean

!apt-get update && !apt-get dist-upgrade -y && !apt-get install -y python3-pip pandoc librsvg2-bin git latexmk texlive-xetex texlive-fonts-extra && apt clean
