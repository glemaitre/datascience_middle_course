import numpy as np

parameter_grid = {
    "polynomialfeatures__degree": np.arange(2, 5),
    "ridge__alpha": np.logspace(1, 3, num=5),
}
