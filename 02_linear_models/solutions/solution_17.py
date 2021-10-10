lasso = Lasso(alpha=1e-2)
lasso.fit(data, target)
lasso.coef_
