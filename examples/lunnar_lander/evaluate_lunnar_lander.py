
"""
训练完成，接下来，我们用stable_baselines3提供的评估函数来评估训练结果：
@see stable_baselines_lunnar_lander.py

@see https://zhuanlan.zhihu.com/p/590272047
@since 2023年12月12日15:12:58
"""

import gym
from stable_baselines import PPO2
from stable_baselines.common.evaluation import evaluate_policy

# Initializing environments is very easy in Gym and can be done via:
env = gym.make("LunarLander-v2")

model = PPO2.load("LunarLander.pkl")

mean_reward, std_reward = evaluate_policy(
    model,
    env,
    deterministic=True,
    render=True,
    n_eval_episodes=5)
print(mean_reward)

env.close()
