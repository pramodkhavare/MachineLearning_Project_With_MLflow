from MLProject.constants import * 
from MLProject.exception import ClassificationException
from MLProject.logger import logging 
from MLProject.utils.main_utils import *
from MLProject.configuration import ConfigurationManager

from six.moves.urllib import request
from zipfile import ZipFile
from pathlib import Path
import os
import urllib.request as request
import zipfile

class DataIngestion:
    def __init__(self, config: ConfigurationManager):
        self.config = config

    def download_file(self) -> None:
        """
        Downloads the file from the source URL if it doesn't already exist locally.
        """
        try:
            local_data_file = Path(self.config.local_data_file)
            local_data_file.parent.mkdir(parents=True, exist_ok=True) 

            if not local_data_file.exists():
                filename, headers = request.urlretrieve(
                    url=self.config.sourse_url,
                    filename=local_data_file
                )
                logging.info(f"{filename} downloaded! with following info: \n{headers}")
            else:
                logging.info(f"File already exists of size: {get_size(local_data_file)}")
        except Exception as e:
            raise ClassificationException(e, sys)

    def extract_zip_file(self) -> None:
        """
        Extracts the zip file into the specified directory.
        """
        try:
            unzip_path = Path(self.config.unzip_dir)
            unzip_path.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logging.info(f"Extracted all files to {unzip_path}")
        except Exception as e:
            raise ClassificationException(e, sys)
