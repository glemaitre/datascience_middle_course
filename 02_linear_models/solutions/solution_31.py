pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(X, y)
