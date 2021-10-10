preprocessor = make_column_transformer(
    (OneHotEncoder(drop="if_binary", handle_unknown="ignore"), selector(dtype_include=object)),
    remainder="passthrough",
    verbose_feature_names_out=False,  # to be less verbose in the feature names
)
preprocessor
