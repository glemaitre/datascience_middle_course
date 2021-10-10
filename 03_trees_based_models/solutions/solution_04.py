_, ax = plt.subplots(figsize=(20, 8))
_ = plot_tree(
    tree, feature_names=X.columns, class_names=class_names, filled=True, ax=ax
)
