classifier = make_pipeline(
    StandardScaler(), LogisticRegression(max_iter=1000)
)
cv_results = cross_validate(
    classifier, X, y, scoring=scoring, n_jobs=-1,
    fit_params={
        "logisticregression__sample_weight": sample_weight
    }
)
cv_results = pd.DataFrame(cv_results)
