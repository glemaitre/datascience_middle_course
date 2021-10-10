from sklearn.linear_model import RidgeCV

model = Pipeline([
    ('preprocess', preprocessing),
    ('classifier', RidgeCV())
])
model.fit(X_train, y_train)
