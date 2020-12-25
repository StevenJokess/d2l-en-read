

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-25 20:01:13
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-25 20:01:50
 * @Description:
 * @TODO::
 * @Reference:https://github.com/thu-ml/tianshou/blob/3d96e3b9d8a111e3533c6f5fb18276640cd5f933/tianshou/policy/__init__.py
-->

from tianshou.policy.base import BasePolicy
from tianshou.policy.random import RandomPolicy
from tianshou.policy.imitation.base import ImitationPolicy
from tianshou.policy.modelfree.dqn import DQNPolicy
from tianshou.policy.modelfree.c51 import C51Policy
from tianshou.policy.modelfree.pg import PGPolicy
from tianshou.policy.modelfree.a2c import A2CPolicy
from tianshou.policy.modelfree.ddpg import DDPGPolicy
from tianshou.policy.modelfree.ppo import PPOPolicy
from tianshou.policy.modelfree.td3 import TD3Policy
from tianshou.policy.modelfree.sac import SACPolicy
from tianshou.policy.modelfree.discrete_sac import DiscreteSACPolicy
from tianshou.policy.modelbase.psrl import PSRLPolicy
from tianshou.policy.multiagent.mapolicy import MultiAgentPolicyManager
