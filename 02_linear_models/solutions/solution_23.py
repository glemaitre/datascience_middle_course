_ = pd.Series(model.coef_[0], index=X.columns).plot.barh()
