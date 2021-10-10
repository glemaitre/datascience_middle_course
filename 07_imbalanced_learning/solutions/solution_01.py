import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.dummy import DummyClassifier

dummy_classifier = DummyClassifier(strategy="most_frequent")
cv_results = cross_validate(dummy_classifier, X, y, n_jobs=-1)
cv_results = pd.DataFrame(cv_results)
cv_results
