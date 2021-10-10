from sklearn.preprocessing import StandardScaler

categorical_encoder = OneHotEncoder(drop="if_binary", handle_unknown='ignore')
numerical_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('imputer', SimpleImputer(strategy='mean'))
])

preprocessing = ColumnTransformer(
    [('cat', categorical_encoder, categorical_columns),
     ('num', numerical_pipe, numerical_columns)])
preprocessing
