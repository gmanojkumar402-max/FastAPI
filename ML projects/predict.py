import joblib
import numpy as np
from typing import Dict, Any

# Load once when this module is imported (good for APIs)
model = joblib.load("linearregression.joblib")
print("Loaded the saved model")

FEATURE_ORDER = [
    "longitude",
    "latitude",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income",
]

def make_prediction(data: Dict[str, Any]) -> float:
    """
    data comes from FastAPI (JSON -> dict).
    Convert dict -> 2D numpy array -> model.predict -> float
    """
    features = np.array([[
        data["longitude"],
        data["latitude"],
        data["housing_median_age"],
        data["total_rooms"],
        data["total_bedrooms"],
        data["population"],
        data["households"],
        data["median_income"],
    ]], dtype=float)

    pred_array = model.predict(features)     # returns array-like
    return float(pred_array[0])              # return scalar
