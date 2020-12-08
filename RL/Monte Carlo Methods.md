

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-08 17:07:37
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-08 17:40:57
 * @Description:
 * @TODO::
 * @Reference:
-->
Follow the instructions in Monte_Carlo.ipynb to write your own implementations of many Monte Carlo methods! The corresponding solutions can be found in Monte_Carlo_Solution.ipynb.[1]

## Monte Carlo Policy Gradients[2]

```py
#[2]
class Policy(nn.Module):
    def __init__(self, s_size=4, h_size=16, a_size=2):
        super(Policy, self).__init__()
        self.fc1 = nn.Linear(s_size, h_size)
        self.fc2 = nn.Linear(h_size, a_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.softmax(x, dim=1)

    def act(self, state):
        state = torch.from_numpy(state).float().unsqueeze(0).to(device)
        probs = self.forward(state).cpu()
        m = Categorical(probs)
        action = m.sample()
        return action.item(), m.log_prob(action)
```


[1]: https://github.com/udacity/deep-reinforcement-learning/blob/master/monte-carlo/Monte_Carlo.ipynbs
[2]: https://github.com/udacity/deep-reinforcement-learning/blob/master/reinforce/REINFORCE.ipynb
