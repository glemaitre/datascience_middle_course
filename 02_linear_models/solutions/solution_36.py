from helper.plotting import DecisionBoundaryDisplay

display = DecisionBoundaryDisplay.from_estimator(
    model, X, cmap=plt.cm.RdBu,
)
_ = moons.plot.scatter(
    x=feature_names[0], y=feature_names[1], c=y,
    s=50, cmap=plt.cm.RdBu, ax=display.ax_
)
