import os
import urllib.request as request
import zipfile
from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.entity.config_entity import DataIngestionConfig
from ChickenDiseaseClassifier.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers= request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded data from {filename} to {headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists, not downloading again")

    # def download_data(self):
    #      # Check if local_data_file exists, if not, download the data from source_URL to local_data_file.
    #     if self.config is None or not hasattr(self.config, 'local_data_file'):
    #         raise ValueError("Configuration is missing 'local_data_file'. Please check your config.")
        
    #     if not os.path.exists(self.data_ingestion_config.local_data_file):
    #         filename, headers = request.urlretrieve(
    #             url=self.config.source_URL,
    #             filename=self.config.local_data_file
    #             )
    #         logger.info(f"Downloaded data from {filename} to {headers}")

    #     else:
    #         logger.info(f"{self.config.local_data_file} already exists, not downloading again")
        

        
    def extract_zip_file(self):
        """
        zip_file_path = self.config.local_data_file
        extract the zip file to the unzip_dir 
        funtion return None
        """
        unzip_path= self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)