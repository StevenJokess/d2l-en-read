#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-06-11 22:25:27
@LastEditors: steven
@LastEditTime: 2020-06-11 22:25:27
@Description:
'''
#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-06-11 22:13:52
@LastEditors: steven
@LastEditTime: 2020-06-11 22:13:52
@Description:
'''
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# https://d2l.ai/chapter_preliminaries/calculus.html
# %% [markdown]
#  Usually, getting better means minimizing a loss function, a score that answers the question “how bad is our model?” This question is more subtle than it appears.
# %% [markdown]
# Ultimately, what we really care about is producing a model that performs well on data that we have never seen before. But we can only fit the model to data that we can actually see.
# %% [markdown]
# the calculation of derivatives
#
# In deep learning, we typically choose loss functions that are differentiable with respect to our model’s parameters.
#
# Put simply, this means that for each parameter, we can determine how rapidly the loss would increase or decrease, were we to increase or decrease that parameter by an infinitesimally small amount.

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
# need to copy from zip :for me, D:\onedrive\文档\code\DL\d2l-en\pytorch\d2l
from d2l import torch as d2l
from IPython import display
import numpy as np

def f(x):
    return 3 * x ** 2 - 4 * x


# %%
get_ipython().run_line_magic('matplotlib', 'inline')
# need to copy from zip :for me, D:\onedrive\文档\code\DL\d2l-en\pytorch\d2l
from d2l import torch as d2l
from IPython import display
import numpy as np

def f(x):
    return 3 * x ** 2 - 4 * x


# %%
def numerical_lim(f, x, h):
    return (f(x + h) - f(x)) / h

h = 0.1
for i in range(5):
    print('h=%.5f, numerical limit=%.5f' % (h, numerical_lim(f, 1, h)))
    h *= 0.1

# %% [markdown]
# In the following, the use_svg_display function specifies the matplotlib package to output the svg figures for sharper images.

# %%
def use_svg_display():  #@save
    """Use the svg format to display a plot in Jupyter."""
    display.set_matplotlib_formats('svg')

# %% [markdown]
# We define the set_figsize function to specify the figure sizes. Note that here we directly use d2l.plt since the import statement from matplotlib import pyplot as plt has been marked for being saved in the d2l package in the preface.
#
#

# %%
def set_figsize(figsize=(3.5, 2.5)):  #@save
    """Set the figure size for matplotlib."""
    use_svg_display()
    d2l.plt.rcParams['figure.figsize'] = figsize


# %%
#@save
def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
    """Set the axes for matplotlib."""
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend:
        axes.legend(legend) # Labeling existing plot elements
    axes.grid()


# %%
#@save
def plot(X, Y=None, xlabel=None, ylabel=None, legend=None, xlim=None,
         ylim=None, xscale='linear', yscale='linear',
         fmts=('-', 'm--', 'g-.', 'r:'), figsize=(3.5, 2.5), axes=None):
    """Plot data instances."""
    if legend is None:
        legend = []

    set_figsize(figsize)
    axes = axes if axes else d2l.plt.gca()# Get Current Axes

    # Return True if `X` (ndarray or list) has 1 axis
    def has_one_axis(X):
        return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list)
                and not hasattr(X[0], "__len__"))

    if has_one_axis(X):
        X = [X]
    if Y is None:
        X, Y = [[]] * len(X), X
    elif has_one_axis(Y):
        Y = [Y]
    if len(X) != len(Y):
        X = X * len(Y)
    axes.cla() # Clear an axes
    for x, y, fmt in zip(X, Y, fmts):
        if len(x):
            axes.plot(x, y, fmt) # plot x and y using fmt
        else:
            axes.plot(y, fmt)
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)

# %% [markdown]
# Get the current Axes instance on the current figure matching the given keyword args, or create one.
#
# Examples:
#
# To get the current polar axes on the current figure:
#
# `plt.gca(projection='polar')`
#
# If the current axes doesn't exist, or isn't a polar one, the appropriate axes will be created and then returned.
#
# ---
#
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.gca.html
# %% [markdown]
# axes.cla()
#
# '''
# Clear an axes,  i.e. the currently active axes in the current figure. It leaves the other axes untouched.
# '''
#
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.cla.
#
# %% [markdown]
# fmts:
# - '-':solid line style 实线;
# - 'm--':magenta dashed line style 紫红色虚线;
# - 'g-':green solid line style 绿色实线；
# - 'r:'red dotted line style 红色点线
#
# ---
#
# For more:
#
# 1. https://blog.csdn.net/leaf_zizi/article/details/87094168
# 2. https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot
# %% [markdown]
# Now we can plot the function  u=f(x)  and its tangent line  y=2x−3  at  x=1 , where the coefficient  2  is the slope of the tangent line.

# %%
x = np.arange(0, 3, 0.1)
plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])

# %% [markdown]
# Exercises:

# %%
x = np.arange(0, 3, 0.1)
#  According to the power rule and multiple rule," 3 * x ** 2 + 1 / (x ** 2) "is the derivative function of f (x).So x == 1,f'(1) ==3 * 1 **2 + 1 / (1 ** 2) == 3 + 1 == 4,tangent line's slope is 4. And we know, tangent line passes the plot (1, 0).So function of the line is " y == 4 * (x - 1) == 4 * x - 4"
plot(x, [x ** 3 - 1 / x, 4 * x - 4], 'x', 'f(x)', legend=['f(x) = x ** 3 - 1 / x ', 'Tangent line (x=1) : y = 4 * x - 4 '])


# %%


