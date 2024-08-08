import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

from src.ml_model.preserve_model import load_model

model_artifacts = load_model(path="models/artifacts.joblib")


def predict_observation(
    df: pd.DataFrame,
    processor_pipeline: Pipeline = model_artifacts["preprocessor"],
    model: LinearRegression = model_artifacts["lc_model"],
) -> np.number:

    obs = processor_pipeline.transform(df)

    # the target was normalized using natural logarithm, so we need to use np.exp to get the actual value
    pred = np.exp(model.predict(obs.reshape(1, -1))[0])
    return pred


if __name__ == "__main__":
    pass
