from sklearn.model_selection import validation_curve

param_name = "n_estimators"
param_range = np.unique(np.logspace(0, 2, num=10).astype(np.int64))
train_scores, test_scores = validation_curve(
    model, X, y, param_name=param_name, param_range=param_range
)
