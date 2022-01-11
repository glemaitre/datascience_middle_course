from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression


numerical_columns_selector = selector(dtype_exclude=object)
numerical_columns = numerical_columns_selector(data)

preprocessor = make_column_transformer(
    (StandardScaler(), numerical_columns),
    (OneHotEncoder(handle_unknown="ignore"), categorical_columns),
)

model = make_pipeline(preprocessor, LogisticRegression(max_iter=1_000))
cv_results = cross_validate(model, data, target)
scores = cv_results["test_score"]
print(f"The accuracy is: {scores.mean():.3f} +/- {scores.std():.3f}")