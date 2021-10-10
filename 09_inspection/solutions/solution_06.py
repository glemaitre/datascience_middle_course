import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import RidgeCV

alphas = np.logspace(-3, 3, num=100)
model = make_pipeline(
    preprocessor, RidgeCV(alphas=alphas)
)
model
