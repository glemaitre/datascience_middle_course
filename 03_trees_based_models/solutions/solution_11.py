from sklearn.ensemble import BaggingClassifier

model = BaggingClassifier(base_estimator=DecisionTreeClassifier())
model.fit(X_train, y_train)
model.score(X_test, y_test)
