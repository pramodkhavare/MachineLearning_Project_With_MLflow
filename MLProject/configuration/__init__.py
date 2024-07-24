from MLProject.entity.config_entity import DataIngestionConfig,DataValidationConfig ,DataTransformationConfig ,ModelTrainerConfig,ModelEvaluationConfig
# from MLProject.entity.artifact_entity import DataIngestionArtifact ,DataTransformationArtifact ,ModelTrainingArtifacts

from MLProject.constants import * 
from MLProject.exception import ClassificationException
from MLProject.logger import logging 
from MLProject.utils.main_utils import *

class ConfigurationManager():
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH ,
                 params_file_path = PARAMS_FILE_PATH ,
                 schema_file_path = SCHEMA_FILE_PATH ,
                 current_time_stamp = CURRENT_TIME_STAMP):
        try:
            self.config_file_path = config_file_path
            self.current_time_stamp = current_time_stamp
            self.params_file_path = params_file_path 
            self.schema_file_path = schema_file_path 
            
            
            self.config = read_yaml(self.config_file_path)
            self.schema = read_yaml(self.schema_file_path)
            self.params = read_yaml(self.params_file_path)
            
             
            create_directories([self.config['artifacts_root']])
        except Exception as e:
            raise ClassificationException (e ,sys)
    def get_data_ingestion_config(self):
        try:
            config = self.config.data_ingestion
            
            data_ingestion_config = DataIngestionConfig(
                root_dir= config.root_dir,
                sourse_url= config.source_URL,
                local_data_file= config.local_data_file,
                unzip_dir= config.unzip_dir
            ) 
            
            return data_ingestion_config
        except Exception as e:
            raise ClassificationException (e ,sys)
        
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        return model_trainer_config
    


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow",
           
        )

        return model_evaluation_config
    

# abc = ConfigurationManager()

# MLProject\configuration\__init__.py