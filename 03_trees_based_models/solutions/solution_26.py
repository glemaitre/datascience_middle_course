%%time
from sklearn.pipeline import make_pipeline

clf = GradientBoostingClassifier(n_estimators=200)
clf.fit(X_train, y_train)
