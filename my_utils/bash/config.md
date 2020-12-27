

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-28 00:18:15
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-28 00:51:11
 * @Description:
 * @TODO::
 * @Reference:
-->
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 9999
# 设置默认目录
c.NotebookApp.notebook_dir = u'/defult/dir/'
# 允许通过任意绑定服务器的ip访问
c.NotebookApp.ip = '*'
# 用于访问的端口
c.NotebookApp.port = 9999
# 不自动打开浏览器
c.NotebookApp.open_browser = False
# 设置SSL认证
c.NotebookApp.certfile = u'/path/to/.jupyter/mycert.pem'
c.NotebookApp.keyfile = u'/path/to/.jupyter/mykey.key'
# 设置登录密码
c.NotebookApp.password = u'sha1:28436903e41b:e36a5f61317d4f515d46178a81834b20ae60d57b'

---

nohup jupyter notebook > jupyter.log &
