

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 17:39:22
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 17:59:05
 * @Description:
 * @TODO::
 * @Reference:
-->

## CartPole-v0

```py
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


[1]: https://github.com/udacity/deep-reinforcement-learning/blob/master/reinforce/REINFORCE.ipynb
[2]: https://github.com/udacity/deep-reinforcement-learning/blob/master/p3_collab-compet/Tennis.ipynb
