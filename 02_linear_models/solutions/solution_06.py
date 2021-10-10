ax = data.plot.scatter(x="Flipper Length (mm)", y="Body Mass (g)")
ax.plot(X, y_pred, label=model.__class__.__name__, color="black", linewidth=4)
_ = ax.legend()
