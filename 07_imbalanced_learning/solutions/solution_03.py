from sklearn.metrics import ConfusionMatrixDisplay

dummy_classifier.fit(X_train, y_train)
display = ConfusionMatrixDisplay.from_estimator(
    dummy_classifier, X_test, y_test
)
