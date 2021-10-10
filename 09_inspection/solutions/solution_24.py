import pandas as pd

importances = pd.DataFrame(
    result.importances[sorted_idx].T,
    columns=X_test.columns[sorted_idx],
)
