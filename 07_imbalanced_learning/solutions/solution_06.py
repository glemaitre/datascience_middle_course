import numpy as np

sample_weight = np.zeros_like(y, dtype=np.float64)
sample_weight[y == "True"] = class_ratio["False"]
sample_weight[y == "False"] = class_ratio["True"]
