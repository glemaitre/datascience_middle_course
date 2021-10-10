%%time
model = make_pipeline(
    StandardScaler(), Nystroem(), LogisticRegression(max_iter=1_000)
)
model.fit(X_train, y_train)
