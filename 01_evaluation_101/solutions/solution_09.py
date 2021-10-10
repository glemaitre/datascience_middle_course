ax = data.plot.scatter(x=data.columns[0], y=data.columns[1])
ax.plot(X["Flipper Length (mm)"], y_pred, color="black", linewidth=4)
_ = ax.set_title("Can I predict penguins' body mass")
