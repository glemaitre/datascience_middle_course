_, ax = plt.subplots(figsize=(8, 6))
ax.errorbar(
    x=param_range,
    y=train_scores.mean(axis=1),
    yerr=train_scores.std(axis=1),
    label="Train score",
)
ax.errorbar(
    x=param_range,
    y=test_scores.mean(axis=1),
    yerr=test_scores.std(axis=1),
    label="Test score",
)
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
ax.set_xscale("log")
ax.set_xlabel("#trees in the forest")
ax.set_ylabel("$R^2#$ score")
_ = ax.set_title("Statistical peformance of random forest")
