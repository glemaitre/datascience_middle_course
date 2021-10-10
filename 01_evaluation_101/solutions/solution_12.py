cv_results = cross_validate(
    model, X, y, cv=cv,
    scoring="r2",
    return_train_score=True
)
cv_results = pd.DataFrame(cv_results)
