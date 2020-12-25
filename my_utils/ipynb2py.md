

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-25 21:59:14
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-25 21:59:26
 * @Description:
 * @TODO::
 * @Reference:https://blog.csdn.net/CBCZJL/article/details/104361123s
-->
现在需要将.ipynb转换为.py文件才可以正常导入。于是在上述代码最后新建一个cell，运行以下代码：

try:
    !jupyter nbconvert --to python file_name.ipynb
    # python即转化为.py，script即转化为.html
    # file_name.ipynb即当前module的文件名
except:
    pass
