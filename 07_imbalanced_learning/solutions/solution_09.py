from sklearn.model_selection import GridSearchCV

param_grid = {
    "randomundersampler__sampling_strategy": np.logspace(-3, -1, num=15)
}
classifier = GridSearchCV(
    make_pipeline_with_sampler(
        StandardScaler(),
        RandomUnderSampler(random_state=42),
        LogisticRegression(max_iter=1000),
    ),
    param_grid=param_grid,
    scoring=make_scorer(
        average_precision_score, needs_proba=True, pos_label="True"
    ),
)
cv_results = cross_validate(
    classifier, X, y, scoring=scoring, n_jobs=-1,
    return_estimator=True,
)
