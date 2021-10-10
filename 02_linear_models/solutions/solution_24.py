display = DecisionBoundaryDisplay.from_estimator(
    model,
    X,
    response_method="decision_function",
    cmap=plt.cm.RdBu,
    plot_method="pcolormesh",
    shading="auto",
)
_ = data.plot.scatter(
    x="Culmen Length (mm)", y="Culmen Depth (mm)", c="Species",
    cmap=plt.cm.RdBu, s=50, ax=display.ax_,
)
