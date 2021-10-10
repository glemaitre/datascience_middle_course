from sklearn.linear_model import RidgeCV

model = make_pipeline(
    PolynomialFeatures(),
    StandardScaler(),
    RidgeCV(alphas=alphas, store_cv_values=True),
)
