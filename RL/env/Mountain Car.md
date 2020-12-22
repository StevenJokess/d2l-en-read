

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-12-22 12:09:46
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-12-22 12:10:12
 * @Description:
 * @TODO::
 * @Reference:https://github.com/aws/amazon-sagemaker-examples/blob/master/reinforcement_learning/rl_mountain_car_coach_gymEnv/rl_mountain_car_coach_gymEnv.ipynb
-->
Mountain Car is a classic control Reinforcement Learning problem that was first introduced by A. Moore in 1991 [1]. An under-powered car is tasked with climbing a steep mountain, and is only successful when it reaches the top. Luckily there's another mountain on the opposite side which can be used to gain momentum, and launch the car to the peak. It can be tricky to find this optimal solution due to the sparsity of the reward. Complex exploration strategies can be used to incentivise exploration of the mountain, but to keep things simple in this example we extend the amount of time in each episode from Open AI Gym's default of 200 environment steps to 10,000 steps, showing how to customise environments. We consider two variants in this example: PatientMountainCar for discrete actions and PatientContinuousMountainCar for continuous actions.

PatientMountainCar¶
Objective: Get the car to the top of the right hand side mountain.
Environment(s): Open AI Gym's MountainCar-v0 that is extended to 10,000 steps per episode.
State: Car's horizontal position and velocity (can be negative).
Action: Direction of push (left, nothing or right).
Reward: -1 for every environment step until success, which incentivises quick solutions.
PatientContinuousMountainCar
Objective: Get the car to the top of the right hand side mountain.
Environment(s): Open AI Gym's MountainCarContinuous-v0 that is extended to 10,000 steps per episode.
State: Car's horizontal position and velocity (can be negative).
Action: Mmagnitude of push (if negative push to left, if positive push to right).
Reward: +100 for reaching top of the right hand side mountain, minus the squared sum of actions from start to end.
