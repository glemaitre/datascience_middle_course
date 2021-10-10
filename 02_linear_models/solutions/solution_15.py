lasso = Lasso(alpha=1e5)
lasso.fit(data, target)
lasso.coef_
