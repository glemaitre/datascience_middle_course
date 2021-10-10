class LinearRegression:
    def __init__(self, intercept=True):
        self.intercept = intercept
    def fit(self, X, y):
        if self.intercept:
            X = np.hstack(
                [X, np.ones((X.shape[0], 1))]
            )
        self.coef_ = coef = np.linalg.inv(X.T @ X) @ X.T @ y
        self._target_name = y.columns
        return self
    def predict(self, X):
        if self.intercept:
            X = np.hstack(
                [X, np.ones((X.shape[0], 1))]
            )
        return pd.DataFrame(
            np.dot(X, coef), columns=self._target_name
        )
