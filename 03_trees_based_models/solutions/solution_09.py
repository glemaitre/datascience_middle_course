from collections import Counter

y_pred_majority = np.array([
    Counter(sample).most_common(1)[0][0]
    for sample in y_pred.T
])
