coef = pd.Series(model.coef_[0], index=X.columns)
_ = coef.plot.barh()
