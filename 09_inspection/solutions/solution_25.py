_, ax = plt.subplots(figsize=(8, 8))
sns.boxplot(data=importances, orient="h", color="tab:blue", ax=ax)
_ = ax.set_title("Permutation Importances (train set)")
