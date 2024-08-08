import numpy as np
import pandas as pd
from joblib import load, dump


def write_model(
    artifacts: dict,
    path: str = "../models/artifacts.joblib",
    dumper=dump,
) -> None:
    # write artifacts to file
    with open(path, "wb") as f:
        dumper(artifacts, f, protocol=5)
        print("Artifacts saved")


def load_model(
    path: str = "../models/artifacts.joblib",
    loader=load,
):
    with open(path, "rb") as f:
        recovered = loader(path)
        return recovered


if __name__ == "__main__":
    pass
