from sklearn.ensemble import RandomForestRegressor

forest = RandomForestRegressor(n_jobs=-1)
forest.fit(X_train, y_train)
forest.score(X_test, y_test)
