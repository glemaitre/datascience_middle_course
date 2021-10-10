coef = pd.Series(pipe[-1].coef_[0], index=X.columns)
_ = coef.plot.barh()
