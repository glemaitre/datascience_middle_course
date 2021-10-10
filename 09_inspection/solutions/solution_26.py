ohe = (model.named_steps['preprocess']
            .named_transformers_['cat'])
feature_names = ohe.get_feature_names_out(categorical_columns)
feature_names = np.r_[feature_names, numerical_columns]
