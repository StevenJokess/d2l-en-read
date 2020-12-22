# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-19 19:05:23
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-12-22 02:03:35
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

---

https://github.com/zhreshold/gluoncv-distro/blob/master/setup.py

#!/usr/bin/env python
import os
from datetime import datetime
import io
import re
import shutil
import sys
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = (
"""GluonCV Python Package
=========================
`GluonCV <https://gluon-cv.mxnet.io>`_ provides implementations of the state-of-the-art (SOTA) deep learning models in computer vision.
It is designed for engineers, researchers, and students to fast prototype products and research ideas based on these models.
Installation
------------
To install, use:
.. code-block:: bash
    pip install gluoncv mxnet-mkl>=1.4.0 --upgrade
To enable different hardware supports such as GPUs, check out  `mxnet variants <https://pypi.org/project/mxnet/>`_.
For example, you can install cuda-9.0 supported mxnet alongside gluoncv:
.. code-block:: bash
    pip install gluoncv mxnet-cu90mkl>=1.4.0 --upgrade
""")

VERSION = find_version('gluoncv', '__init__.py')

if 'TRAVIS_TAG' in os.environ and os.environ['TRAVIS_TAG'].startswith('patch-'):
    VERSION = os.environ['TRAVIS_TAG'].split('-')[1]
elif 'APPVEYOR_REPO_TAG_NAME' in os.environ and os.environ['APPVEYOR_REPO_TAG_NAME'].startswith('patch-'):
    VERSION = os.environ['APPVEYOR_REPO_TAG_NAME'].split('-')[1]
elif 'TRAVIS_TAG' in os.environ or 'APPVEYOR_REPO_TAG_NAME' in os.environ:
    pass
else:
    VERSION += 'b{0}'.format(datetime.today().strftime('%Y%m%d'))

requirements = [
    'numpy',
    'tqdm',
    'requests',
    # 'mxnet',
    'matplotlib',
    'portalocker',
    'Pillow',
    'scipy',
    'tensorboardx',
    'decord',
    'opencv-python',
    'yacs',
    'pandas',
    'pyyaml',
    'autocfg',
    'autogluon.core'
]

setup(
    # Metadata
    name='gluoncv',
    version=VERSION,
    author='Gluon CV Toolkit Contributors',
    url='https://github.com/dmlc/gluon-cv',
    description='MXNet Gluon CV Toolkit',
    long_description=long_description,
    license='Apache-2.0',

    # Package info
    packages=find_packages(exclude=('docs', 'tests', 'scripts')),
    zip_safe=True,
    include_package_data=True,
    install_requires=requirements,
)
