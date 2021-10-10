summary = pd.DataFrame()
summary["Tree test score"] = cv_results[["test_score"]]
summary["Dummy test score"] = cv_results_dummy[["test_score"]]
summary["Permuted error"] = errors_permutation
