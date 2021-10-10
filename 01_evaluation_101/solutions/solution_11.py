for cv_idx, (train, test) in enumerate(cv.split(X, y)):
    ax = data.iloc[train].plot.scatter(x=data.columns[0], y=data.columns[1], color="tab:orange")
    data.iloc[test].plot.scatter(x=data.columns[0], y=data.columns[1], ax=ax)
    ax.set_title(f"Fold #{cv_idx}")
