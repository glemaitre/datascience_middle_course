from sklearn.linear_model import Ridge

alphas = np.logspace(-2, 2, num=50)

model = GridSearchCV(
    make_pipeline(
        PolynomialFeatures(),
        StandardScaler(),
        Ridge(),
    ),
    param_grid={
        "ridge__alpha": alphas
    },
    scoring="neg_mean_squared_error",
)
model
