_, ax = plt.subplots(figsize=(8, 6))
ax = sns.boxplot(data=coef, orient='h', ax=ax, color="tab:blue")
ax.set_title("Coefficients during cross-validation")
_ = ax.vlines(0, 0, len(X.columns), linestyle="--", alpha=0.4, color="black")
