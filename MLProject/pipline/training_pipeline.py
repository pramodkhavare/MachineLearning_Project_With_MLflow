from MLProject.configuration import ConfigurationManager
from MLProject.components.data_ingestion import DataIngestion
from MLProject.components.data_validation import DataValiadtion
from MLProject.components.data_transformation import DataTransformation
from MLProject.components.model_trainer import ModelTrainer
from MLProject.components.model_evaluation import ModelEvaluation
from MLProject.logger import logging
from MLProject.exception import ClassificationException

import os ,sys
import pandas as pd
import uuid
from threading import Thread
from collections import namedtuple
from datetime import datetime


class TrainPipeline():
    def __init__(self ,config : ConfigurationManager):
        try:
            self.config = config 
            
        except Exception as e:
            raise ClassificationException (e ,sys) from e
        
    def start_data_ingestion(self):
        try:
            data_ingestion_config = self.config.get_data_ingestion_config()
            
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise ClassificationException (e ,sys) from e
        
    def start_data_Validation(self):
        try:
            data_validation_config = self.config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns() 
            
        except Exception as e:
            raise ClassificationException (e ,sys) from e
    
    def start_data_transformation(self):
        try:
            data_transformation_config = self.config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
            
        except Exception as e:
            raise ClassificationException (e ,sys) from e
        
    def start_model_training(self):
        try:
            model_training_config = self.config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_training_config)
            model_trainer.train() 
             
        except Exception as e:
            raise ClassificationException (e ,sys) from e
        
    def start_model_evaluation(self):
        try:
            model_evaluation_config = self.config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config= model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise ClassificationException (e ,sys) from e
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion() 
            data_validation_artifacts = self.start_data_Validation()
            data_transformation_artifacts = self.start_data_transformation()
            model_training_artifacts = self.start_model_training()
            model_evaluation_artifacts = self.start_model_evaluation()
        except Exception as e:
            raise ClassificationException (e ,sys) from e
        
    def run(self):
        try:
            self.run_pipeline() 
        except Exception as e:
            raise ClassificationException (e ,sys) from e
        