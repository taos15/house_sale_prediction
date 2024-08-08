"""This is the home page of the streamlit app"""

from pandas import isna
from pydantic import InstanceOf
import streamlit as st
import numpy as np
import pandas as pd

from src.ml_model.predict_ovservation import predict_observation
from src.ml_model.preserve_model import load_model
from src.types.data_fields import data

# from ml_model.preserve_model import load_model
# from ..ml_model.preserve_model import load_model


# Initial dictionary
testObservation = {
    "MSSubClass": [60],
    "MSZoning": ["RL"],
    "LotFrontage": [65.0],
    "LotArea": [8450],
    "Street": ["Pave"],
    "Alley": [np.NaN],
    "LotShape": ["Reg"],
    "LandContour": ["Lvl"],
    "Utilities": ["AllPub"],
    "LotConfig": ["Inside"],
    "LandSlope": ["Gtl"],
    "Neighborhood": ["CollgCr"],
    "Condition1": ["Norm"],
    "Condition2": ["Norm"],
    "BldgType": ["1Fam"],
    "HouseStyle": ["2Story"],
    "OverallQual": [7],
    "OverallCond": [5],
    "YearBuilt": [2003],
    "YearRemodAdd": [2003],
    "RoofStyle": ["Gable"],
    "RoofMatl": ["CompShg"],
    "Exterior1st": ["VinylSd"],
    "Exterior2nd": ["VinylSd"],
    "MasVnrType": ["BrkFace"],
    "MasVnrArea": [196.0],
    "ExterQual": ["Gd"],
    "ExterCond": ["TA"],
    "Foundation": ["PConc"],
    "BsmtQual": ["Gd"],
    "BsmtCond": ["TA"],
    "BsmtExposure": ["No"],
    "BsmtFinType1": ["GLQ"],
    "BsmtFinSF1": [706],
    "BsmtFinType2": ["Unf"],
    "BsmtFinSF2": [0],
    "BsmtUnfSF": [150],
    "TotalBsmtSF": [856],
    "Heating": ["GasA"],
    "HeatingQC": ["Ex"],
    "CentralAir": ["Y"],
    "Electrical": ["SBrkr"],
    "1stFlrSF": [856],
    "2ndFlrSF": [854],
    "LowQualFinSF": [0],
    "GrLivArea": [1710],
    "BsmtFullBath": [1],
    "BsmtHalfBath": [0],
    "FullBath": [2],
    "HalfBath": [1],
    "BedroomAbvGr": [3],
    "KitchenAbvGr": [1],
    "KitchenQual": ["Gd"],
    "TotRmsAbvGrd": [8],
    "Functional": ["Typ"],
    "Fireplaces": [0],
    "FireplaceQu": ["NaN"],
    "GarageType": ["Attchd"],
    "GarageYrBlt": [2003.0],
    "GarageFinish": ["RFn"],
    "GarageCars": [2],
    "GarageArea": [548],
    "GarageQual": ["TA"],
    "GarageCond": ["TA"],
    "PavedDrive": ["Y"],
    "WoodDeckSF": [0],
    "OpenPorchSF": [61],
    "EnclosedPorch": [0],
    "3SsnPorch": [0],
    "ScreenPorch": [0],
    "PoolArea": [0],
    "PoolQC": ["N"],
    "Fence": ["N"],
    "MiscFeature": ["N"],
    "MiscVal": [0],
    "MoSold": [2],
    "YrSold": [2008],
    "SaleType": ["WD"],
    "SaleCondition": ["Normal"],
    "PropertyAge": [5],
}

# load the model's artifacts
artifacts = load_model("models/artifacts.joblib")

# place holder to the current value of the files
result_holder = {}


def homepage():
    """This is the homepage component"""

    st.set_page_config(
        page_title="Test Observation",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Test Observation Input Form")
    generate_sliders(observation=data)


def generate_sliders(observation: dict, result: dict = result_holder):

    for key, value in observation.items():

        if "options" in observation[key].keys():
            # Add more strings as options for the dropdown here
            result[key] = [
                st.selectbox(
                    f"{observation[key]['name']}",
                    options=[
                        list(obj.values())[0]
                        for obj in observation[key][
                            "options"
                        ]  # get the description of options
                    ],
                    index=0,
                    # f"{key}", options=artifacts["categorial_options"][key], index=0
                )
            ]
        elif "minValue" in observation[key].keys():
            result[key] = st.slider(
                f"{key}",
                min_value=observation[key]["minValue"],
                max_value=observation[key]["minValue"] + 10,  # until I add max value
                # max_value=observation[key]["maxValue"],
                value=observation[key]["value"],
            )

    # st.write("### Updated Test Observation Dictionary")
    # updated_dict = {
    #     key: replace_nan(st.session_state[key]) for key in testObservation.keys()
    # }
    # st.json(updated_dict)

    print(f"------This is result holder: {pd.DataFrame(result)}------\n\n")
    print(
        f"------This is the prediction: {predict_observation(pd.DataFrame(result))}-----"
    )


if __name__ == "__main__":
    homepage()
