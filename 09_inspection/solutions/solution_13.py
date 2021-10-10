preprocessor.fit(X)
coef = [estimator[-1].coef_ for estimator in cv_results["estimator"]]
coef = pd.DataFrame(coef, columns=preprocessor.get_feature_names_out(X.columns))
