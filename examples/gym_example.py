
"""
what's gym? providing a standard API to communicate between learning algorithms and environments

use pip install gym[all] to install all dependencies.

@see https://github.com/openai/gym
@since 2023年12月5日16:59:35
"""

import gym
# Initializing environments is very easy in Gym and can be done via:
# 报错 AttributeError: module 'gym.envs.box2d' has no attribute 'LunarLander'  pip install Box2D
env = gym.make("LunarLander-v2")
env.reset()

while True:
    env.render()
    # This will just create a sample action in any environment.
    # In this environment, the action can be any of one how in list on 4, for example [0 1 0 0]
    action = env.action_space.sample()

    # this executes the environment with an action,
    # and returns the observation of the environment,
    # the reward, if the env is over, and other info.
    observation, reward, done, info = env.step(action)
    print(observation, reward, done, info, action)
    if done:
        break

env.close()
