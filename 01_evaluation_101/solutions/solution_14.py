from sklearn.model_selection import permutation_test_score

model = LinearRegression()
score, permutation_score, pvalue = permutation_test_score(
    model, X, y, cv=cv,
    n_jobs=-1, n_permutations=30
)
errors_permutation = pd.Series(permutation_score, name="Permuted error")
