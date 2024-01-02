
"""
Optuna 的经典监督分类问题
Our goal is to find the value of x that minimizes the output of the objective function.
This is the “optimization.” During the optimization, Optuna repeatedly calls and evaluates the objective function with different values of x.

@since 2023年12月21日17:45:29
"""

import optuna
import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines import PPO2


def objective(trial):
    env = gym.make('LunarLander-v2')
    # suggest_params = {"gamma": 0.999, "n_steps": 1024, "ent_coef": 0.01, "lam": 0.98, "nminibatches": 32 }
    # 1e8指的是1乘以10的8次方100000000
    # 1e-8指的是1乘以10的-8次方 0.00000001
    suggest_params = {
        # suggest_discrete_uniform 提供离散参数的 suggestion.
        # 该值是从 [low,high] 中采样的，并且其离散化的步数是:math:q. 更具体地说，该方法返回 low,low+q,low+2q,…,low+kq≤high 序列中的一个值，
        # 其中:math:k 代表一个整数。
        # TypeError: 'numpy.float64' object cannot be interpreted as an integer
        'n_steps': int(trial.suggest_discrete_uniform('n_steps', 0, 2048, 32)),
        'gamma': trial.suggest_loguniform('gamma', 0.9, 0.9999),
        'ent_coef': trial.suggest_loguniform('ent_coef', 1e-8, 1e-1),
        'lam': trial.suggest_uniform('lam', 0.8, 1.)
    }
    model = PPO2(MlpPolicy, env, verbose=1, **suggest_params)
    model.learn(total_timesteps=1500000)

    obs = env.reset()
    state = None
    done = False
    score = 0
    while not done:
        action, _states = model.predict(obs, state=state)
        obs, reward, done, info = env.step(action)
        score += reward
    return score


if __name__ == '__main__':
    study = optuna.create_study(storage="sqlite:///example.db", direction="maximize")
    study.optimize(objective, n_trials=100)
    best_params = study.best_params
    best_value = study.best_value
    # Found best_params: {'ent_coef': 0.023121911942027683, 'gamma': 0.9945887603584302, 'lam': 0.9666637725688133, 'n_steps': 128.0}, best_value: 274.92360131847454
    print("Found best_params: {}, best_value: {}".format(best_params, best_value))

