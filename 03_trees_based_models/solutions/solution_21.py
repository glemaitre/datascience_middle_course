for boosting_round, tree in enumerate(adaboost.estimators_):
    _, ax = plt.subplots(figsize=(8, 6))
    display = DecisionBoundaryDisplay.from_estimator(
        tree, X, response_method="predict", cmap=plt.cm.viridis,
        alpha=0.4,
        ax=ax,
    )
    data.plot.scatter(
        x="Culmen Length (mm)",
        y="Culmen Depth (mm)",
        c="Species",
        s=80,
        cmap=plt.cm.viridis,
        alpha=0.5,
        edgecolor="black",
        ax=ax,
    )
    _ = ax.set_title(f"Decision tree trained at round {boosting_round}")
