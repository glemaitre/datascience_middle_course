cv_results = cross_validate(
    model, X, y, cv=cv,
    return_estimator=True, return_train_score=True,
    n_jobs=-1,
)
cv_results = pd.DataFrame(cv_results)
