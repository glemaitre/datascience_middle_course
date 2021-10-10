ax = cv_results[["train_score", "test_score"]].plot.hist(bins=30, alpha=0.8)
ax.set_xlim([0, 1])
_ = ax.legend(loc="upper left")
