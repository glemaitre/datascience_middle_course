result = permutation_importance(
    model, X_train, y_train, n_repeats=10,
    random_state=42, n_jobs=2
)
sorted_idx = result.importances_mean.argsort()
