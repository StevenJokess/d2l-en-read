# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-19 19:05:23
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-19 19:24:07
Description:
TODO::
Reference:https://github.com/thu-ml/tianshou/blob/master/setup.py
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def get_version() -> str:
    # https://packaging.python.org/guides/single-sourcing-package-version/
    init = open(os.path.join("tianshou", "__init__.py"), "r").read().split()
    return init[init.index("__version__") + 2][1:-1]

setup(
    name="tianshou",
    version=get_version(),
    description="A Library for Deep Reinforcement Learning",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/thu-ml/tianshou",
    author="TSAIL",
    author_email="trinkle23897@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="reinforcement learning platform pytorch",
    packages=find_packages(
        exclude=["test", "test.*", "examples", "examples.*", "docs", "docs.*"]
    ),
    install_requires=[
        "gym>=0.15.4",
        "tqdm",
        "numpy",
        "tensorboard",
        "torch>=1.4.0",
        "numba>=0.51.0",
    ],
    extras_require={
        "dev": [
            "Sphinx",
            "sphinx_rtd_theme",
            "sphinxcontrib-bibtex",
            "flake8",
            "pytest",
            "pytest-cov",
            "ray>=1.0.0",
            "mypy",
            "pydocstyle",
            "doc8",
        ],
        "atari": ["atari_py", "cv2"],
        "mujoco": ["mujoco_py"],
        "pybullet": ["pybullet"],
    },
)

---
# https://github.com/qqiang00/Reinforce/blob/master/setup.py
from setuptools import setup, find_packages

setup(
    name = 'reinforce',
    packages = find_packages(),
)

---
# https://github.com/yenchenlin/rl-attack-detection/blob/master/setup.py
from setuptools import setup, find_packages
import sys

if sys.version_info.major != 3:
    print("This Python is only compatible with Python 3, but you are running "
          "Python {}. The installation will likely fail.".format(sys.version_info.major))

setup(name='baselines',
      packages=[package for package in find_packages()
                if package.startswith('baselines')],
      install_requires=[
          'gym>=0.9.1',
          'scipy',
          'tqdm',
          'joblib',
          'zmq',
          'dill',
          'tensorflow >= 1.0.0',
          'azure==1.0.3',
          'progressbar2',
      ],
      description="OpenAI baselines: high quality implementations of reinforcement learning algorithms",
      author="OpenAI",
      url='https://github.com/openai/baselines',
      author_email="gym@openai.com",
      version="0.1.3")
