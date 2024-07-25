import joblib 
import numpy as np 
import pandas as pd 
from pathlib import Path



class PredictionPipeline:
    def __init__(self ,model_path ):
        self.model_path = model_path 
        # self.preprocessor_path = preprocessor_path 
    
    def prediction(self ,data):
        model = joblib.load(self.model_path) 
        prediction = model.predict(data)
        
        return prediction