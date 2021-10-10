import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
y_pred = model.predict(X_test)

n_bootstrap = 100
bootstrap_score = []
for _ in range(n_bootstrap):
    bootstrap_indices = rng.choice(
        np.arange(y_pred.size), size=y_pred.size, replace=True
    )
    bootstrap_score.append(
        r2_score(y_test.to_numpy()[bootstrap_indices], y_pred[bootstrap_indices])
    )
plt.hist(bootstrap_score)
plt.xlim([0, 1])
_ = plt.title("R2 score distribution using bootstrap sampling")
