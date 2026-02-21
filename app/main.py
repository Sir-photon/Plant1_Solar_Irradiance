from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


# Load the trained model and feature order
model = joblib.load('/Model/solar_model2.pkl')
feature = joblib.load('feature_columns.pkl')

app = FastAPI(title='Solar Irradiation Forecast API')

# Input schema
class InputData(BaseModel):
    AMBIENT_TEMPERATURE : float
    MODULE_TEMPERATURE: float
    Irr_lag_1: float
    Irr_lag_4:float
    Irr_lag_24:float
    Irr_rolling_std: float
    Irr_rolling_mean:float
    hour_sin:float
    hour_cos:float
    day_sin:float
    day_cos:float
    month_sin: float
    month_cos: float

@app.get('/')
def home():
    return {'Message': 'Solar Forecast API is running'}

@app.post('/predict')
def predict(data: InputData):
    #input_df = pd.DataFrame([data.dict()])
    input_df = pd.DataFrame([data.model_dump()])
    input_df = input_df[feature]
    prediction = model.predict(input_df)[0]
    return {'Predicted Irradiation: ': float(prediction)}