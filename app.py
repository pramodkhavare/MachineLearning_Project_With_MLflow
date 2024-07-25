from flask import Flask ,request 
import os ,sys
import pip 
import json 
from flask import render_template ,abort ,send_file
from pathlib import Path
import pandas as pd 


from MLProject.pipline.prediction_pipeline import PredictionPipeline

MODEL_PATh = r"D:\Data Science\MachineLearning\Project\UnderProcessProject\MachineLearning_Project_With_MLflow\artifacts\model_trainer\model.joblib"
 
app = Flask(__name__)   #app is Flask object

@app.route('/' ,methods=['GET' ,'POST'])
def homepage():
    return render_template("index.html") 


@app.route('/predict',methods=['GET' ,'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    else:
        fixed_acidity = float(request.form.get('fixed_acidity'))
        volatile_acidity = float(request.form.get('volatile_acidity'))
        citric_acid = float(request.form.get('citric_acid'))
        residual_sugar = float(request.form.get('residual_sugar'))
        chlorides = float(request.form.get('chlorides'))
        free_sulfur_dioxide = float(request.form.get('free_sulfur_dioxide'))
        total_sulfur_dioxide = float(request.form.get('total_sulfur_dioxide'))
        density = float(request.form.get('density'))
        pH = float(request.form.get('pH'))
        sulphates = float(request.form.get('sulphates'))
        alcohol = float(request.form.get('alcohol'))
        
        
        data_dictionary = {
            'fixed acidity' : [fixed_acidity] ,
            'volatile acidity' :[volatile_acidity] ,
             'citric acid' : [citric_acid] ,
             'residual sugar' : [residual_sugar] ,
             'chlorides' : [chlorides] ,
             'free sulfur dioxide' : [free_sulfur_dioxide] ,
             'total sulfur dioxide' : [total_sulfur_dioxide] ,
             'density' : [density] ,
             'pH' : [pH] ,
             'sulphates' : [sulphates] ,
             'alcohol' : [alcohol] 
        }
        
        df = pd.DataFrame(data_dictionary)
        
        pipeline = PredictionPipeline(model_path=MODEL_PATh)
        
        predicted_data = pipeline.prediction(df)  
        
        results=round(predicted_data[0],2)
        
        return render_template('form.html',final_result=results)

        
        
if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port= 8080 ,debug=True)