import numpy as np

coef = np.linalg.inv(X.T @ X) @ X.T @ y
coef
