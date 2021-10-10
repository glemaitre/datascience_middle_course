from sklearn.preprocessing import PolynomialFeatures

model = make_pipeline(
    PolynomialFeatures(degree=3), StandardScaler(), LogisticRegression()
)
model.fit(X, y)
