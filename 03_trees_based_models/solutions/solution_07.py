for tree in forest:
    X_train_bootstrap, y_train_bootstrap = bootstrap_sample(X_train, y_train)
    tree.fit(X_train_bootstrap, y_train_bootstrap)
