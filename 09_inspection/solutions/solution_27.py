_, ax = plt.subplots(figsize=(8, 6))
coef = pd.Series(
    model[-1].coef_,
    index=feature_names,
)
coef.plot.barh(ax=ax)
_ = ax.set_title("Model coefficients")
