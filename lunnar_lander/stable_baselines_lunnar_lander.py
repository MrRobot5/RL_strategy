
"""
利用 stable_baselines 训练 LunarLander

训练效果查看：
    1. tensorboard.exe --logdir /d/export/LunarLander-v2/
    2. TensorBoard 1.15.0 at http://localhost:6006/

ref: https://zhuanlan.zhihu.com/p/406517851
@since 2023年12月12日10:34:04
"""

import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

env = gym.make('LunarLander-v2')

# Optional: PPO2 requires a vectorized environment to run
# the env is now wrapped automatically when passing it to the constructor
# env = DummyVecEnv([lambda: env])

# 策略网络为 MLP
# verbose: (int) the verbosity level: 0 none, 1 training information, 2 tensorflow debug
# tensorboard_log: (str) the log location for tensorboard (if None, no logging)
model = PPO2(MlpPolicy, env, gamma=0.999, n_steps=1024, ent_coef=0.01, lam=0.98, nminibatches=32, verbose=1, tensorboard_log="/export/LunarLander-v2/")
model.learn(total_timesteps=1500000)
# model = PPO2.load("./LunarLander.pkl")
# Save the current parameters to file
model.save("LunarLander_150K")

obs = env.reset()
done = False
score = 0
while not done:
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    score += reward
    env.render()
env.close()
print(score)