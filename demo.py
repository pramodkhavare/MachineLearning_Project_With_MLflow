
from MLProject.pipline.training_pipeline import TrainPipeline
from MLProject.logger import logging 
from MLProject.exception import ClassificationException
from MLProject.configuration import ConfigurationManager
# from Housing.src.components.data_validation import DataValidation
from MLProject.components.data_ingestion import DataIngestion
# from Housing.src.components.data_transformation import DataTransformation
from MLProject.components.model_trainer import *


def main():
    try:
        pipeline = TrainPipeline(config=ConfigurationManager())
        print(12)
        pipeline.run()

    except Exception as e:
        logging.error(f"{e}")

        

if __name__ == "__main__":
    # main()
    pipeline = TrainPipeline(config=ConfigurationManager())
    pipeline.run()