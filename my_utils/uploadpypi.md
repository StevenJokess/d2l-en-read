

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-07 20:27:33
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-07 20:35:16
 * @Description:
 * @TODO::
 * @Reference:https://nbdev.fast.ai/tutorial.html#Upload-to-pypi
-->

## Upload to pypi

If you want people to be able to install your project by just typing pip install your-project then you need to upload it to pypi. The good news is, we've already created a fully pypi compliant installer for your project! So all you need to do is register at pypi (click "Register" on pypi) if you haven't previously done so, and then create a file called
 ~/.pypirc
with your login details. It should have these contents:

```
[pypi]
username = your_pypi_username
password = your_pypi_password
```

Another thing you will need is twine, so you should run once

```sh
pip install twine
```

https://pypi.org/project/twine/
https://twine.readthedocs.io/en/latest/
https://github.com/pypa/twine

To upload your project to pypi, just type make pypi in your project root directory. Once it's complete, a link to your project on pypi will be printed.

NB: if you are not using the make release command to upload to both conda and pypi (described below), you must increment the version number in settings.ini each time you want to push a new release to pypi.

## Upload to pypi and conda (recommended)

The command `make release` from the root of your nbdev repo will bump the version of your module and upload your project to both conda and pypi. We recommend this approach as it is the easiest way to publish packages.
