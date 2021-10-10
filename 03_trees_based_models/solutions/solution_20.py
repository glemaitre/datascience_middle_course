from sklearn.ensemble import AdaBoostClassifier

base_estimator = DecisionTreeClassifier(max_depth=3, random_state=0)
adaboost = AdaBoostClassifier(
    base_estimator=base_estimator,
    n_estimators=3, algorithm="SAMME",
    random_state=0
)
adaboost.fit(X, y)
