from sklearn.dummy import DummyRegressor

dummy_model = DummyRegressor(strategy="mean")
cv_results_dummy = cross_validate(
    dummy_model, X, y, cv=cv,
    scoring="r2",
    return_train_score=True
)
cv_results_dummy = pd.DataFrame(cv_results_dummy)
