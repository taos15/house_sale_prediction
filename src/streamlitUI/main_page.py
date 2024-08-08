"""This is the home page of the streamlit app"""

from pandas import isna
from pydantic import InstanceOf
import streamlit as st
import numpy as np


def homepage():
    """This is the homepage component"""

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

    st.set_page_config(
        page_title="Test Observation",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Test Observation Input Form")

    # Function to handle NaN values in dictionary
    def replace_nan(value):
        return None if isinstance(value, float) and np.isnan(value) else value

    for key, value in testObservation.items():

        if isinstance(value[0], str):
            # Add more strings as options for the dropdown here
            st.selectbox(f"{key}", options=["Option1", "Option2", value[0]], index=2)
        elif isinstance(value[0], (int, float)):
            st.slider(
                f"{key}",
                min_value=0,
                max_value=int(max(100, value[0])),
                value=0 if np.isnan(value[0]) else int(value[0]),
            )

    # st.write("### Updated Test Observation Dictionary")
    # updated_dict = {
    #     key: replace_nan(st.session_state[key]) for key in testObservation.keys()
    # }
    # st.json(updated_dict)

    if __name__ == "__main__":
        pass
