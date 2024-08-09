"""This is the home page of the streamlit app"""

from pandas import isna
from pydantic import InstanceOf
import streamlit as st
import numpy as np
import pandas as pd

from src.ml_model.predict_ovservation import predict_observation
from src.ml_model.preserve_model import load_model
from src.types_utils.data_fields import data

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
result_holder: dict = testObservation.copy()

main_features_list = [
    "LotArea",
    # "OverallQual",
    # "OverallCond",
    "YearBuilt",
    "YrSold",
    # "MasVnrArea",
    "TotalBsmtSF",
    "Heating",
    "CentralAir",
    "GrLivArea",
    "BedroomAbvGr",
    "FullBath",
    "HalfBath",
    "GarageCars",
    "PropertyAge",
]


def homepage():
    """This is the homepage component"""

    st.set_page_config(
        page_title="Test Observation",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    tab1, tab2, tab3 = st.tabs(["Predict", "Graph", "About"])

    col1, col2 = st.columns([1, 3])

    with tab1:
        st.subheader(
            f"Current prediction: ${np.round(predict_observation(pd.DataFrame(result_holder)),2):,.2f}"
        )

        # with col1:
        #     main_col = col1.container(height=1000) # it messes the expander

        st.title("Modify the inputs to get a prediction")
    generate_sliders(
        observation=data,
        main_features=main_features_list,
        render_zone=tab1,  # it messes the expander
    )


def generate_sliders(
    observation: dict,
    render_zone: st._DeltaGenerator = st,  # type: ignore
    result: dict = result_holder,
    main_features: list = [],
):
    # create main area
    with render_zone:
        rend_container = st.container(height=500)

    # creates a container to display the most import features on top
    primary_features_area = rend_container.container()
    footage_features = (
        primary_features_area.container()
    )  # create a container to group the footage features
    year_features = (
        primary_features_area.container()
    )  # create a container to group the footage features

    # creates a container inside an expander to hide the extra features
    with rend_container.expander("Advance Options"):
        advance_area = st.container()

    def render_categorical_area(obj_key: str, opt: dict, container=rend_container):
        # Display the selectbox with the values (descriptions)
        selected_value = container.selectbox(
            # selected_value = st.selectbox(
            f"{observation[obj_key]['name']}",
            help=f"{observation[obj_key]['description']}",
            options=list(opt.keys()),  # display the values
            index=0,
        )

        # Store the key corresponding to the selected value
        result[obj_key] = [opt[selected_value]]

    def render_numerical_area(obj_key: str, container=rend_container):
        if obj_key == "PropertyAge":
            age_value = result["YrSold"][0] - result["YearBuilt"][0]
            year_features.text(f"PropertyAge: {age_value if age_value > 0 else 0}")
            result[obj_key] = [age_value]
        else:
            result[obj_key] = [
                container.slider(
                    # st.slider(
                    f"{obj_key}",
                    help=f"{observation[obj_key]['description']}",
                    min_value=observation[obj_key]["minValue"],
                    max_value=observation[obj_key]["maxValue"],
                    value=np.round(observation[obj_key]["defaultValue"]),
                    step=1.0,
                )
            ]

    for key in observation.keys():

        # create the categorical selects
        if "options" in observation[key].keys():
            # Create a mapping of values to keys
            options_map = {
                list(obj.values())[0]: list(obj.keys())[0]
                for obj in observation[key]["options"]
            }

            if (key) in main_features:

                render_categorical_area(key, options_map, primary_features_area)
            else:
                render_categorical_area(key, options_map, advance_area)

        # create the numerical selects
        elif "minValue" in observation[key].keys():
            if (key) in main_features:
                # group the footages features
                if key in ["LotArea", "GrLivArea", "TotalBsmtSF"]:
                    render_numerical_area(key, footage_features)
                    # group the year features
                elif key in ["YearBuilt", "YrSold"]:
                    render_numerical_area(key, year_features)
                else:
                    render_numerical_area(key, primary_features_area)
            else:
                render_numerical_area(key, advance_area)

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
