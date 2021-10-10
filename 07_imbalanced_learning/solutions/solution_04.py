from sklearn.metrics import make_scorer
from sklearn.metrics import (
    balanced_accuracy_score,
    precision_score,
    recall_score,
    average_precision_score,
)

scoring = {
    "balanced_accuracy": make_scorer(balanced_accuracy_score),
    "precision": make_scorer(precision_score, pos_label="True"),
    "recall": make_scorer(recall_score, pos_label="True"),
    "average_precision": make_scorer(
        average_precision_score, needs_proba=True, pos_label="True"
    ),
}

cv_results = cross_validate(
    dummy_classifier, X, y, scoring=scoring, n_jobs=-1
)
cv_results = pd.DataFrame(cv_results)
cv_results
