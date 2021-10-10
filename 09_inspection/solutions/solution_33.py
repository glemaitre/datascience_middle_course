print("Computing partial dependence plots...")
display = PartialDependenceDisplay.from_estimator(
    model,
    X_train,
    numerical_columns,
    kind="both",
    subsample=50,
    n_jobs=3,
    grid_resolution=20,
    random_state=0,
    ice_lines_kw={"color": "tab:blue", "alpha": 0.2, "linewidth": 0.5},
    pd_line_kw={"color": "tab:orange", "linestyle": "--"},
)
