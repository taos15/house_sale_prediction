"""this file host the options for every data field"""

data = {
    "MSSubClass": {
        "name": "MSSubClass",
        "description": "Identifies the type of dwelling involved in the sale.",
        "options": [
            {20: "1-STORY 1946 & NEWER ALL STYLES"},
            {30: "1-STORY 1945 & OLDER"},
            {40: "1-STORY W/FINISHED ATTIC ALL AGES"},
            {45: "1-1/2 STORY - UNFINISHED ALL AGES"},
            {50: "1-1/2 STORY FINISHED ALL AGES"},
            {60: "2-STORY 1946 & NEWER"},
            {70: "2-STORY 1945 & OLDER"},
            {75: "2-1/2 STORY ALL AGES"},
            {80: "SPLIT OR MULTI-LEVEL"},
            {85: "SPLIT FOYER"},
            {90: "DUPLEX - ALL STYLES AND AGES"},
            {120: "1-STORY PUD (Planned Unit Development) - 1946 & NEWER"},
            {150: "1-1/2 STORY PUD - ALL AGES"},
            {160: "2-STORY PUD - 1946 & NEWER"},
            {180: "PUD - MULTILEVEL - INCL SPLIT LEV/FOYER"},
            {190: "2 FAMILY CONVERSION - ALL STYLES AND AGES"},
        ],
    },
    "MSZoning": {
        "name": "MSZoning",
        "description": "Identifies the general zoning classification of the sale.",
        "options": [
            {"A": "Agriculture"},
            {"C": "Commercial"},
            {"FV": "Floating Village Residential"},
            {"I": "Industrial"},
            {"RH": "Residential High Density"},
            {"RL": "Residential Low Density"},
            {"RP": "Residential Low Density Park"},
            {"RM": "Residential Medium Density"},
        ],
    },
    "LotFrontage": {
        "name": "LotFrontage",
        "description": "Linear feet of street connected to property",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "LotArea": {
        "name": "LotArea",
        "description": "Lot size in square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "Street": {
        "name": "Street",
        "description": "Type of road access to property",
        "options": [{"Grvl": "Gravel"}, {"Pave": "Paved"}],
    },
    "Alley": {
        "name": "Alley",
        "description": "Type of alley access to property",
        "options": [{"Grvl": "Gravel"}, {"Pave": "Paved"}, {"NA": "No alley access"}],
    },
    "LotShape": {
        "name": "LotShape",
        "description": "General shape of property",
        "options": [
            {"Reg": "Regular"},
            {"IR1": "Slightly irregular"},
            {"IR2": "Moderately Irregular"},
            {"IR3": "Irregular"},
        ],
    },
    "LandContour": {
        "name": "LandContour",
        "description": "Flatness of the property",
        "options": [
            {"Lvl": "Near Flat/Level"},
            {
                "Bnk": "Banked - Quick and significant rise from street grade to building"
            },
            {"HLS": "Hillside - Significant slope from side to side"},
            {"Low": "Depression"},
        ],
    },
    "Utilities": {
        "name": "Utilities",
        "description": "Type of utilities available",
        "options": [
            {"AllPub": "All public Utilities (E,G,W,& S)"},
            {"NoSewr": "Electricity, Gas, and Water (Septic Tank)"},
            {"NoSeWa": "Electricity and Gas Only"},
            {"ELO": "Electricity only"},
        ],
    },
    "LotConfig": {
        "name": "LotConfig",
        "description": "Lot configuration",
        "options": [
            {"Inside": "Inside lot"},
            {"Corner": "Corner lot"},
            {"CulDSac": "Cul-de-sac"},
            {"FR2": "Frontage on 2 sides of property"},
            {"FR3": "Frontage on 3 sides of property"},
        ],
    },
    "LandSlope": {
        "name": "LandSlope",
        "description": "Slope of property",
        "options": [
            {"Gtl": "Gentle slope"},
            {"Mod": "Moderate Slope"},
            {"Sev": "Severe Slope"},
        ],
    },
    "Neighborhood": {
        "name": "Neighborhood",
        "description": "Physical locations within Ames city limits",
        "options": [
            {"Blmngtn": "Bloomington Heights"},
            {"Blueste": "Bluestem"},
            {"BrDale": "Briardale"},
            {"BrkSide": "Brookside"},
            {"ClearCr": "Clear Creek"},
            {"CollgCr": "College Creek"},
            {"Crawfor": "Crawford"},
            {"Edwards": "Edwards"},
            {"Gilbert": "Gilbert"},
            {"IDOTRR": "Iowa DOT and Rail Road"},
            {"MeadowV": "Meadow Village"},
            {"Mitchel": "Mitchell"},
            {"Names": "North Ames"},
            {"NoRidge": "Northridge"},
            {"NPkVill": "Northpark Villa"},
            {"NridgHt": "Northridge Heights"},
            {"NWAmes": "Northwest Ames"},
            {"OldTown": "Old Town"},
            {"SWISU": "South & West of Iowa State University"},
            {"Sawyer": "Sawyer"},
            {"SawyerW": "Sawyer West"},
            {"Somerst": "Somerset"},
            {"StoneBr": "Stone Brook"},
            {"Timber": "Timberland"},
            {"Veenker": "Veenker"},
        ],
    },
    "Condition1": {
        "name": "Condition1",
        "description": "Proximity to various conditions",
        "options": [
            {"Artery": "Adjacent to arterial street"},
            {"Feedr": "Adjacent to feeder street"},
            {"Norm": "Normal"},
            {"RRNn": "Within 200' of North-South Railroad"},
            {"RRAn": "Adjacent to North-South Railroad"},
            {"PosN": "Near positive off-site feature--park, greenbelt, etc."},
            {"PosA": "Adjacent to positive off-site feature"},
            {"RRNe": "Within 200' of East-West Railroad"},
            {"RRAe": "Adjacent to East-West Railroad"},
        ],
    },
    "Condition2": {
        "name": "Condition2",
        "description": "Proximity to various conditions (if more than one is present)",
        "options": [
            {"Artery": "Adjacent to arterial street"},
            {"Feedr": "Adjacent to feeder street"},
            {"Norm": "Normal"},
            {"RRNn": "Within 200' of North-South Railroad"},
            {"RRAn": "Adjacent to North-South Railroad"},
            {"PosN": "Near positive off-site feature--park, greenbelt, etc."},
            {"PosA": "Adjacent to positive off-site feature"},
            {"RRNe": "Within 200' of East-West Railroad"},
            {"RRAe": "Adjacent to East-West Railroad"},
        ],
    },
    "BldgType": {
        "name": "BldgType",
        "description": "Type of dwelling",
        "options": [
            {"1Fam": "Single-family Detached"},
            {
                "2FmCon": "Two-family Conversion; originally built as one-family dwelling"
            },
            {"Duplx": "Duplex"},
            {"TwnhsE": "Townhouse End Unit"},
            {"TwnhsI": "Townhouse Inside Unit"},
        ],
    },
    "HouseStyle": {
        "name": "HouseStyle",
        "description": "Style of dwelling",
        "options": [
            {"1Story": "One story"},
            {"1.5Fin": "One and one-half story: 2nd level finished"},
            {"1.5Unf": "One and one-half story: 2nd level unfinished"},
            {"2Story": "Two story"},
            {"2.5Fin": "Two and one-half story: 2nd level finished"},
            {"2.5Unf": "Two and one-half story: 2nd level unfinished"},
            {"SFoyer": "Split Foyer"},
            {"SLvl": "Split Level"},
        ],
    },
    "OverallQual": {
        "name": "OverallQual",
        "description": "Rates the overall material and finish of the house",
        "options": [
            {10: "Very Excellent"},
            {9: "Excellent"},
            {8: "Very Good"},
            {7: "Good"},
            {6: "Above Average"},
            {5: "Average"},
            {4: "Below Average"},
            {3: "Fair"},
            {2: "Poor"},
            {1: "Very Poor"},
        ],
    },
    "OverallCond": {
        "name": "OverallCond",
        "description": "Rates the overall condition of the house",
        "options": [
            {10: "Very Excellent"},
            {9: "Excellent"},
            {8: "Very Good"},
            {7: "Good"},
            {6: "Above Average"},
            {5: "Average"},
            {4: "Below Average"},
            {3: "Fair"},
            {2: "Poor"},
            {1: "Very Poor"},
        ],
    },
    "YearBuilt": {
        "name": "YearBuilt",
        "description": "Original construction date",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "YearRemodAdd": {
        "name": "YearRemodAdd",
        "description": "Remodel date (same as construction date if no remodeling or additions)",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "RoofStyle": {
        "name": "RoofStyle",
        "description": "Type of roof",
        "options": [
            {"Flat": "Flat"},
            {"Gable": "Gable"},
            {"Gambrel": "Gabrel (Barn)"},
            {"Hip": "Hip"},
            {"Mansard": "Mansard"},
            {"Shed": "Shed"},
        ],
    },
    "RoofMatl": {
        "name": "RoofMatl",
        "description": "Roof material",
        "options": [
            {"ClyTile": "Clay or Tile"},
            {"CompShg": "Standard (Composite) Shingle"},
            {"Membran": "Membrane"},
            {"Metal": "Metal"},
            {"Roll": "Roll"},
            {"Tar&Grv": "Gravel & Tar"},
            {"WdShake": "Wood Shakes"},
            {"WdShngl": "Wood Shingles"},
        ],
    },
    "Exterior1st": {
        "name": "Exterior1st",
        "description": "Exterior covering on house",
        "options": [
            {"AsbShng": "Asbestos Shingles"},
            {"AsphShn": "Asphalt Shingles"},
            {"BrkComm": "Brick Common"},
            {"BrkFace": "Brick Face"},
            {"CBlock": "Cinder Block"},
            {"CemntBd": "Cement Board"},
            {"HdBoard": "Hard Board"},
            {"ImStucc": "Imitation Stucco"},
            {"MetalSd": "Metal Siding"},
            {"Other": "Other"},
            {"Plywood": "Plywood"},
            {"PreCast": "PreCast"},
            {"Stone": "Stone"},
            {"Stucco": "Stucco"},
            {"VinylSd": "Vinyl Siding"},
            {"Wd Sdng": "Wood Siding"},
            {"WdShing": "Wood Shingles"},
        ],
    },
    "Exterior2nd": {
        "name": "Exterior2nd",
        "description": "Exterior covering on house (if more than one material)",
        "options": [
            {"AsbShng": "Asbestos Shingles"},
            {"AsphShn": "Asphalt Shingles"},
            {"BrkComm": "Brick Common"},
            {"BrkFace": "Brick Face"},
            {"CBlock": "Cinder Block"},
            {"CemntBd": "Cement Board"},
            {"HdBoard": "Hard Board"},
            {"ImStucc": "Imitation Stucco"},
            {"MetalSd": "Metal Siding"},
            {"Other": "Other"},
            {"Plywood": "Plywood"},
            {"PreCast": "PreCast"},
            {"Stone": "Stone"},
            {"Stucco": "Stucco"},
            {"VinylSd": "Vinyl Siding"},
            {"Wd Sdng": "Wood Siding"},
            {"WdShing": "Wood Shingles"},
        ],
    },
    "MasVnrType": {
        "name": "MasVnrType",
        "description": "Masonry veneer type",
        "options": [
            {"BrkCmn": "Brick Common"},
            {"BrkFace": "Brick Face"},
            {"CBlock": "Cinder Block"},
            {"None": "None"},
            {"Stone": "Stone"},
        ],
    },
    "MasVnrArea": {
        "name": "MasVnrArea",
        "description": "Masonry veneer area in square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "ExterQual": {
        "name": "ExterQual",
        "description": "Evaluates the quality of the material on the exterior",
        "options": [
            {"Ex": "Excellent"},
            {"Gd": "Good"},
            {"TA": "Average/Typical"},
            {"Fa": "Fair"},
            {"Po": "Poor"},
        ],
    },
    "ExterCond": {
        "name": "ExterCond",
        "description": "Evaluates the present condition of the material on the exterior",
        "options": [
            {"Ex": "Excellent"},
            {"Gd": "Good"},
            {"TA": "Average/Typical"},
            {"Fa": "Fair"},
            {"Po": "Poor"},
        ],
    },
    "Foundation": {
        "name": "Foundation",
        "description": "Type of foundation",
        "options": [
            {"BrkTil": "Brick & Tile"},
            {"CBlock": "Cinder Block"},
            {"PConc": "Poured Concrete"},
            {"Slab": "Slab"},
            {"Stone": "Stone"},
            {"Wood": "Wood"},
        ],
    },
    "BsmtQual": {
        "name": "BsmtQual",
        "description": "Evaluates the height of the basement",
        "options": [
            {"Ex": "Excellent (100+ inches)"},
            {"Gd": "Good (90-99 inches)"},
            {"TA": "Typical (80-89 inches)"},
            {"Fa": "Fair (70-79 inches)"},
            {"Po": "Poor (<70 inches)"},
            {"NA": "No Basement"},
        ],
    },
    "BsmtCond": {
        "name": "BsmtCond",
        "description": "Evaluates the general condition of the basement",
        "options": [
            {"Ex": "Excellent"},
            {"Gd": "Good"},
            {"TA": "Typical - slight dampness allowed"},
            {"Fa": "Fair - dampness or some cracking or settling"},
            {"Po": "Poor - Severe cracking, settling, or wetness"},
            {"NA": "No Basement"},
        ],
    },
    "BsmtExposure": {
        "name": "BsmtExposure",
        "description": "Refers to walkout or garden level walls",
        "options": [
            {"Gd": "Good Exposure"},
            {
                "Av": "Average Exposure (split levels or foyers typically score average or above)"
            },
            {"Mn": "Minimum Exposure"},
            {"No": "No Exposure"},
            {"NA": "No Basement"},
        ],
    },
    "BsmtFinType1": {
        "name": "BsmtFinType1",
        "description": "Rating of basement finished area",
        "options": [
            {"GLQ": "Good Living Quarters"},
            {"ALQ": "Average Living Quarters"},
            {"BLQ": "Below Average Living Quarters"},
            {"Rec": "Average Rec Room"},
            {"LwQ": "Low Quality"},
            {"Unf": "Unfinished"},
            {"NA": "No Basement"},
        ],
    },
    "BsmtFinSF1": {
        "name": "BsmtFinSF1",
        "description": "Type 1 finished square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "BsmtFinType2": {
        "name": "BsmtFinType2",
        "description": "Rating of basement finished area (if multiple types)",
        "options": [
            {"GLQ": "Good Living Quarters"},
            {"ALQ": "Average Living Quarters"},
            {"BLQ": "Below Average Living Quarters"},
            {"Rec": "Average Rec Room"},
            {"LwQ": "Low Quality"},
            {"Unf": "Unfinished"},
            {"NA": "No Basement"},
        ],
    },
    "BsmtFinSF2": {
        "name": "BsmtFinSF2",
        "description": "Type 2 finished square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "BsmtUnfSF": {
        "name": "BsmtUnfSF",
        "description": "Unfinished square feet of basement area",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "TotalBsmtSF": {
        "name": "TotalBsmtSF",
        "description": "Total square feet of basement area",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "Heating": {
        "name": "Heating",
        "description": "Type of heating",
        "options": [
            {"Floor": "Floor Furnace"},
            {"GasA": "Gas forced warm air furnace"},
            {"GasW": "Gas hot water or steam heat"},
            {"Grav": "Gravity furnace"},
            {"OthW": "Hot water or steam heat other than gas"},
            {"Wall": "Wall furnace"},
        ],
    },
    "HeatingQC": {
        "name": "HeatingQC",
        "description": "Heating quality and condition",
        "options": [
            {"Ex": "Excellent"},
            {"Gd": "Good"},
            {"TA": "Average/Typical"},
            {"Fa": "Fair"},
            {"Po": "Poor"},
        ],
    },
    "CentralAir": {
        "name": "CentralAir",
        "description": "Central air conditioning",
        "options": [{"N": "No"}, {"Y": "Yes"}],
    },
    "Electrical": {
        "name": "Electrical",
        "description": "Electrical system",
        "options": [
            {"SBrkr": "Standard Circuit Breakers & Romex"},
            {"FuseA": "Fuse Box over 60 AMP and all Romex wiring (Average)"},
            {"FuseF": "60 AMP Fuse Box and mostly Romex wiring (Fair)"},
            {"FuseP": "60 AMP Fuse Box and mostly knob & tube wiring (poor)"},
            {"Mix": "Mixed"},
        ],
    },
    "1stFlrSF": {
        "name": "1stFlrSF",
        "description": "First Floor square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "2ndFlrSF": {
        "name": "2ndFlrSF",
        "description": "Second floor square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "LowQualFinSF": {
        "name": "LowQualFinSF",
        "description": "Low quality finished square feet (all floors)",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "GrLivArea": {
        "name": "GrLivArea",
        "description": "Above grade (ground) living area square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "BsmtFullBath": {
        "name": "BsmtFullBath",
        "description": "Basement full bathrooms",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "BsmtHalfBath": {
        "name": "BsmtHalfBath",
        "description": "Basement half bathrooms",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "FullBath": {
        "name": "FullBath",
        "description": "Full bathrooms above grade",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "HalfBath": {
        "name": "HalfBath",
        "description": "Half baths above grade",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "BedroomAbvGr": {
        "name": "BedroomAbvGr",
        "description": "Bedrooms above grade (does NOT include basement bedrooms)",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "KitchenAbvGr": {
        "name": "KitchenAbvGr",
        "description": "Kitchens above grade",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "KitchenQual": {
        "name": "KitchenQual",
        "description": "Kitchen quality",
        "options": [
            {"Ex": "Excellent"},
            {"Gd": "Good"},
            {"TA": "Typical/Average"},
            {"Fa": "Fair"},
            {"Po": "Poor"},
        ],
    },
    "TotRmsAbvGrd": {
        "name": "TotRmsAbvGrd",
        "description": "Total rooms above grade (does not include bathrooms)",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "Functional": {
        "name": "Functional",
        "description": "Home functionality (Assume typical unless deductions are warranted)",
        "options": [
            {"Typ": "Typical Functionality"},
            {"Min1": "Minor Deductions 1"},
            {"Min2": "Minor Deductions 2"},
            {"Mod": "Moderate Deductions"},
            {"Maj1": "Major Deductions 1"},
            {"Maj2": "Major Deductions 2"},
            {"Sev": "Severely Damaged"},
            {"Sal": "Salvage only"},
        ],
    },
    "Fireplaces": {
        "name": "Fireplaces",
        "description": "Number of fireplaces",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "FireplaceQu": {
        "name": "FireplaceQu",
        "description": "Fireplace quality",
        "options": [
            {"Ex": "Excellent - Exceptional Masonry Fireplace"},
            {"Gd": "Good - Masonry Fireplace in main level"},
            {
                "TA": "Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement"
            },
            {"Fa": "Fair - Prefabricated Fireplace in basement"},
            {"Po": "Poor - Ben Franklin Stove"},
            {"NA": "No Fireplace"},
        ],
    },
    "GarageType": {
        "name": "GarageType",
        "description": "Garage location",
        "options": [
            {"2Types": "More than one type of garage"},
            {"Attchd": "Attached to home"},
            {"Basment": "Basement Garage"},
            {
                "BuiltIn": "Built-In (Garage part of house - typically has room above garage)"
            },
            {"CarPort": "Car Port"},
            {"Detchd": "Detached from home"},
            {"NA": "No Garage"},
        ],
    },
    "GarageYrBlt": {
        "name": "GarageYrBlt",
        "description": "Year garage was built",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "GarageFinish": {
        "name": "GarageFinish",
        "description": "Interior finish of the garage",
        "options": [
            {"Fin": "Finished"},
            {"RFn": "Rough Finished"},
            {"Unf": "Unfinished"},
            {"NA": "No Garage"},
        ],
    },
    "GarageCars": {
        "name": "GarageCars",
        "description": "Size of garage in car capacity",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "GarageArea": {
        "name": "GarageArea",
        "description": "Size of garage in square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "GarageQual": {
        "name": "GarageQual",
        "description": "Garage quality",
        "options": [
            {"Ex": "Excellent"},
            {"Gd": "Good"},
            {"TA": "Typical/Average"},
            {"Fa": "Fair"},
            {"Po": "Poor"},
            {"NA": "No Garage"},
        ],
    },
    "GarageCond": {
        "name": "GarageCond",
        "description": "Garage condition",
        "options": [
            {"Ex": "Excellent"},
            {"Gd": "Good"},
            {"TA": "Typical/Average"},
            {"Fa": "Fair"},
            {"Po": "Poor"},
            {"NA": "No Garage"},
        ],
    },
    "PavedDrive": {
        "name": "PavedDrive",
        "description": "Paved driveway",
        "options": [{"Y": "Paved"}, {"P": "Partial Pavement"}, {"N": "Dirt/Gravel"}],
    },
    "WoodDeckSF": {
        "name": "WoodDeckSF",
        "description": "Wood deck area in square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "OpenPorchSF": {
        "name": "OpenPorchSF",
        "description": "Open porch area in square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "EnclosedPorch": {
        "name": "EnclosedPorch",
        "description": "Enclosed porch area in square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "3SsnPorch": {
        "name": "3SsnPorch",
        "description": "Three season porch area in square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "ScreenPorch": {
        "name": "ScreenPorch",
        "description": "Screen porch area in square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "PoolArea": {
        "name": "PoolArea",
        "description": "Pool area in square feet",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "PoolQC": {
        "name": "PoolQC",
        "description": "Pool quality",
        "options": [
            {"Ex": "Excellent"},
            {"Gd": "Good"},
            {"TA": "Average/Typical"},
            {"Fa": "Fair"},
            {"NA": "No Pool"},
        ],
    },
    "Fence": {
        "name": "Fence",
        "description": "Fence quality",
        "options": [
            {"GdPrv": "Good Privacy"},
            {"MnPrv": "Minimum Privacy"},
            {"GdWo": "Good Wood"},
            {"MnWw": "Minimum Wood/Wire"},
            {"NA": "No Fence"},
        ],
    },
    "MiscFeature": {
        "name": "MiscFeature",
        "description": "Miscellaneous feature not covered in other categories",
        "options": [
            {"Elev": "Elevator"},
            {"Gar2": "2nd Garage (if not described in garage section)"},
            {"Othr": "Other"},
            {"Shed": "Shed (over 100 SF)"},
            {"TenC": "Tennis Court"},
            {"NA": "None"},
        ],
    },
    "MiscVal": {
        "name": "MiscVal",
        "description": "$Value of miscellaneous feature",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "MoSold": {
        "name": "MoSold",
        "description": "Month Sold (MM)",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "YrSold": {
        "name": "YrSold",
        "description": "Year Sold (YYYY)",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
    "SaleType": {
        "name": "SaleType",
        "description": "Type of sale",
        "options": [
            {"WD": "Warranty Deed - Conventional"},
            {"CWD": "Warranty Deed - Cash"},
            {"VWD": "Warranty Deed - VA Loan"},
            {"New": "Home just constructed and sold"},
            {"COD": "Court Officer Deed/Estate"},
            {"Con": "Contract 15% Down payment regular terms"},
            {"ConLw": "Contract Low Down payment and low interest"},
            {"ConLI": "Contract Low Interest"},
            {"ConLD": "Contract Low Down"},
            {"Oth": "Other"},
        ],
    },
    "SaleCondition": {
        "name": "SaleCondition",
        "description": "Condition of sale",
        "options": [
            {"Normal": "Normal Sale"},
            {"Abnorml": "Abnormal Sale - trade, foreclosure, short sale"},
            {"AdjLand": "Adjoining Land Purchase"},
            {
                "Alloca": "Allocation - two linked properties with separate deeds, typically condo with a garage unit"
            },
            {"Family": "Sale between family members"},
            {
                "Partial": "Home was not completed when last assessed (associated with New Homes)"
            },
        ],
    },
    "PropertyAge": {
        "name": "YrSold",
        "description": "Year Sold (YYYY)",
        "minValue": 0.0,
        "maxValue": 0.0,
        "value": 0.0,
        "defaultValue": 0.0,
    },
}
