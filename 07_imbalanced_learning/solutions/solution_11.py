param_grid = {
    "randomundersampler__sampling_strategy": np.logspace(-2.5, 0, num=15)
}
classifier = GridSearchCV(
    make_pipeline_with_sampler(
        StandardScaler(),
        RandomUnderSampler(random_state=42),
        LogisticRegression(max_iter=1000),
    ),
    param_grid=param_grid,
    scoring="balanced_accuracy",
    n_jobs=-1
)
cv_results = cross_validate(
    classifier, X, y, scoring=benefit_matrix, return_estimator=True,
)
cv_results = pd.DataFrame(cv_results)
