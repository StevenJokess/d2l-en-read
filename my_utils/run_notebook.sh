


###
 # @version:
 # @Author:  StevenJokess https://github.com/StevenJokess
 # @Date: 2020-11-28 00:40:51
 # @LastEditors:  StevenJokess https://github.com/StevenJokess
 # @LastEditTime: 2020-11-28 00:41:02
 # @Description:
 # @TODO::
 # @Reference:https://github.com/jantic/DeOldify/blob/master/run_notebook.sh
###
jupyter notebook --port=8888 --no-browser --allow-root --ip=0.0.0.0 --NotebookApp.token="" --NotebookApp.password="$(./set_password.py $NOTEBOOK_PASSWORD)"
