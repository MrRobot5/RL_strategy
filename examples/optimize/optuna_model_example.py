

"""
Re-use the best trial
在超参数优化后再次使用最佳超参数重新评估目标函数。

ref: https://optuna.readthedocs.io/en/stable/tutorial/20_recipes/010_reuse_best_trial.html

@since 2023年12月25日 10:51:14
"""
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import optuna


def objective(trial):
    X, y = make_classification(n_features=10, random_state=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    C = trial.suggest_loguniform("C", 1e-7, 10.0)

    clf = LogisticRegression(C=C)
    clf.fit(X_train, y_train)

    return clf.score(X_test, y_test)


def detailed_objective(trial):
    # Use same code objective to reproduce the best model
    X, y = make_classification(n_features=10, random_state=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    C = trial.params["C"]

    clf = LogisticRegression(C=C)
    clf.fit(X_train, y_train)

    # calculate more evaluation metrics
    pred = clf.predict(X_test)

    acc = metrics.accuracy_score(pred, y_test)
    recall = metrics.recall_score(pred, y_test)
    precision = metrics.precision_score(pred, y_test)
    f1 = metrics.f1_score(pred, y_test)

    return acc, f1, recall, precision


study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=10)
# Show the best value.
print(study.best_trial.value)

# best_trial提供了一个接口，用于使用当前最佳超参数值重新评估目标函数。
# calculate acc, f1, recall, and precision
acc, f1, recall, precision = detailed_objective(study.best_trial)
print(acc, f1, recall, precision)
