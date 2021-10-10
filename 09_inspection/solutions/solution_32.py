from sklearn.ensemble import RandomForestClassifier

model = Pipeline([
    ('preprocess', preprocessing),
    ('classifier', RandomForestClassifier(random_state=42))
])
model.fit(X_train, y_train)
