import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge

model = make_pipeline(
    preprocessor, Ridge(alpha=100_000)
)
model
