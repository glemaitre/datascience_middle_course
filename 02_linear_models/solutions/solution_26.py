_, ax = plt.subplots(figsize=(8, 8))
ax = sns.kdeplot(
    data=X_train_scaled,
    x="Culmen Length (mm)",
    y="Culmen Depth (mm)",
    levels=10,
    fill=True,
    cmap=plt.cm.viridis,
    ax=ax,
)
_ = ax.axis("square")
