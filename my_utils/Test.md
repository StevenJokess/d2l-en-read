

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-27 19:06:34
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-27 19:06:42
 * @Description:
 * @TODO::
 * @Reference:https://github.com/openai/EPG
-->
Testing
First, set theta_load_path = '<path_to_theta.npy>/theta.npy' in launch_local.py according to the theta.npy obtained after running the launch_local.py script. This file should be located in /<home_dir>/EPG_experiments/<month>-<day>/<experiment_name>/thetas/.

Then run:

PYTHONPATH=. python epg/launch_local.py --test true
