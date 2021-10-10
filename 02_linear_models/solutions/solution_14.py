coef = pd.Series(lasso.coef_, index=feature_names)
_ = coef.plot.barh()
