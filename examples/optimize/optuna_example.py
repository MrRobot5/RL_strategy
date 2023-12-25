
"""
Optuna 的经典监督分类问题
Our goal is to find the value of x that minimizes the output of the objective function.
This is the “optimization.” During the optimization, Optuna repeatedly calls and evaluates the objective function with different values of x.

@since 2023年12月21日17:45:29
"""

import optuna


def objective(trial):
    """
    In optuna, conventionally functions to be optimized are named objective.
    suggest_float() selects parameters uniformly within the range provided.
    """
    x = trial.suggest_uniform("x", -9, 10)
    return (x - 2) ** 2


if __name__ == '__main__':
    # To start the optimization, we create a study object and pass the objective function to method optimize() as follows.
    study = optuna.create_study(storage="sqlite:///example.db")
    study.optimize(objective, n_trials=100)
    # You can get the best parameter as follows.
    best_params = study.best_params
    # To get the best observed value of the objective function
    best_value = study.best_value
    found_x = best_params["x"]
    print("Found x: {}, (x - 2)^2: {}".format(found_x, (found_x - 2) ** 2))

