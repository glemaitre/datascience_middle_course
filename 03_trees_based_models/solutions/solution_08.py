y_pred = np.array([
    tree.predict(X_test) for tree in forest
])
