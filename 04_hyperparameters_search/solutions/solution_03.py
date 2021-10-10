from collections import defaultdict
from sklearn.model_selection import cross_val_score

search_results = defaultdict(list)
for degree in parameter_grid["polynomialfeatures__degree"]:
    for alpha in parameter_grid["ridge__alpha"]:
        search_results["polynomialfeatures__degree"].append(degree)
        search_results["ridge__alpha"].append(alpha)
        model.set_params(
            polynomialfeatures__degree=degree,
            ridge__alpha=alpha,
        )
        search_results["score"].append(cross_val_score(model, X_train, y_train))
search_results = pd.DataFrame(search_results)
