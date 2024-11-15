from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

app = FastAPI()

class InputData(BaseModel):

    Age: float
    Gender: str
    Tenure: float
    Usage_Frequency: float
    Support_Calls: float
    Payment_Delay: float
    Subscription_Type: str
    Contract_Length: str 
    Total_Spend: float
    Last_Interaction: float

#indicar el folder donde tienen guardado el modelo/ los modelos
model = joblib.load('models\RandomForestClassifier_model.pkl')

@app.get("/")
async def read_root():
    return {"health_check": "OK", "model_version": 1}

@app.post("/predict")
async def predict(input_data: InputData):
    
        df = pd.DataFrame([input_data.model_dump().values()], 
                          columns=input_data.model_dump().keys())
        pred = model.predict(df)
        return {"predicted_class": int(pred[0])}