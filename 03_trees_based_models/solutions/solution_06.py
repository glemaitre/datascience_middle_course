from sklearn.tree import DecisionTreeClassifier

n_trees = 5
forest = [DecisionTreeClassifier() for _ in range(n_trees)]
