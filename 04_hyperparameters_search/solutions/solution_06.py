best_model = model.set_params(
    polynomialfeatures__degree=search_results["polynomialfeatures__degree"].iloc[0],
    ridge__alpha=search_results["ridge__alpha"].iloc[0],
)
