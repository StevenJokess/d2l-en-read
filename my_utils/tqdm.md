

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 22:16:46
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 22:17:01
 * @Description:
 * @TODO::
 * @Reference:https://github.com/tqdm/tqdm
-->

```
from tqdm import tqdm
for i in tqdm(range(10000)):
```

76%|████████████████████████        | 7568/10000 [00:33<00:10, 229.00it/s]

trange(N) can be also used as a convenient shortcut for tqdm(range(N)).
