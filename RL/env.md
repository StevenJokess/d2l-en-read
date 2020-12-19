

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 17:39:22
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-19 19:27:05
 * @Description:
 * @TODO::
 * @Reference:https://gym.openai.com/docs/
-->

## 初始化

```py
#[5]

env = gym.make('CartPole-v0')

初始化
env = gym.make('CartPole-v0')
# 定义使用gym库中的某一个环境，'CartPole-v0'可以改为其它环境
env = env.unwrapped
# 据说不做这个动作会有很多限制，unwrapped是打开限制的意思



```

## 各个参数的获取

```py
#[5]
env.action_space
# 查看这个环境中可用的action有多少个，返回Discrete()格式
env.observation_space
# 查看这个环境中observation的特征，返回Box()格式
n_actions=env.action_space.n
# 查看这个环境中可用的action有多少个，返回int
n_features=env.observation_space.shape[0]
# 查看这个环境中observation的特征有多少个，返回int

print(env.action_space)             # 查看这个环境中可用的action有多少个，返回Discrete()格式
print(env.observation_space)        # 查看这个环境中observation的特征，返回Box()格式
```


## CartPole-v0
```
#[1]

env = gym.make('CartPole-v0')

state = env.reset()
for t in range(1000):
    action, _ = policy.act(state)
    env.render()
    state, reward, done, _ = env.step(action)
    if done:
        break

env.close()
```




## Unity

https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation.md

```py

from unityagents import UnityEnvironment
env = UnityEnvironment(file_name="...")
```

### Tennis[2]


Mac: "path/to/Tennis.app"
Windows (x86): "path/to/Tennis_Windows_x86/Tennis.exe"
Windows (x86_64): "path/to/Tennis_Windows_x86_64/Tennis.exe"
Linux (x86): "path/to/Tennis_Linux/Tennis.x86"
Linux (x86_64): "path/to/Tennis_Linux/Tennis.x86_64"
Linux (x86, headless): "path/to/Tennis_Linux_NoVis/Tennis.x86"
Linux (x86_64, headless): "path/to/Tennis_Linux_NoVis/Tennis.x86_64"

### Soccer[3]


Mac: "path/to/Soccer.app"
Windows (x86): "path/to/Soccer_Windows_x86/Soccer.exe"
Windows (x86_64): "path/to/Soccer_Windows_x86_64/Soccer.exe"
Linux (x86): "path/to/Soccer_Linux/Soccer.x86"
Linux (x86_64): "path/to/Soccer_Linux/Soccer.x86_64"
Linux (x86, headless): "path/to/Soccer_Linux_NoVis/Soccer.x86"
Linux (x86_64, headless): "path/to/Soccer_Linux_NoVis/Soccer.x86_64"

## close

```py
#[4]
from gym.utils import closer

env_closer = closer.Closer()
```

---

## 刷新环境

```py
env.reset()
# 用于一个世代（done）后环境的重启，获取回合的第一个observation
env.render()
# 用于每一步后刷新环境状态


observation_, reward, done, info = env.step(action)
# 获取下一步的环境、得分、检测是否完成。
```


[1]: https://github.com/udacity/deep-reinforcement-learning/blob/master/reinforce/REINFORCE.ipynb
[2]: https://github.com/udacity/deep-reinforcement-learning/blob/master/p3_collab-compet/Tennis.ipynb
[3]: https://github.com/udacity/deep-reinforcement-learning/blob/master/p3_collab-compet/Soccer.ipynb
[4]: https://github.com/openai/gym/blob/master/gym/core.py
[5]: https://blog.csdn.net/weixin_44791964/article/details/96767972
