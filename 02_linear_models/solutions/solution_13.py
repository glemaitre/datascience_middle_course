from sklearn.linear_model import Lasso

lasso = Lasso(alpha=1)
lasso.fit(data, target)
lasso.coef_
