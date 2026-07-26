import os
import sys
import shutil
import config.config as config
from src.utils.logger_config import logger
from src.utils.schemas import dataSource as ds
from src.utils.responses import ResponseStatus as response




class KaggleExtractor:

    def __init__(self, kaggle_api):
        self.api = kaggle_api
        self. current_data_dir = config.get_data_dir(source_name=ds.KAGGLE.value)


    def clean_data_directory(self):
        if os.path.exists(self.current_data_dir):
            shutil.rmtree(self.current_data_dir)
        os.makedirs(self.current_data_dir, exist_ok=True)

    def is_data_exists(self) -> bool:
        
        if os.path.exists(self.current_data_dir) and os.listdir(self.current_data_dir):
            files = [os.path.join(self.current_data_dir, f) for f in os.listdir(self.current_data_dir)]
            if any(os.path.getsize(f) > 0 for f in files):
                return True
        return False


    def download_dataset(self, dataset_name):
        
        if self.is_data_exists():
            return True
            
        try:
            self.clean_data_directory()
            logger.info(response.DOWNLOAD_DATASET_START.value.format(dataset_name=dataset_name))

            self.api.dataset_download_files(
                dataset_name,
                path=self.current_data_dir, 
                unzip=True
            )
            
             
            if self.is_data_exists():
                logger.info(response.DOWNLOAD_DATASET_SUCCESS.value.format(
                    dataset_name=dataset_name, 
                    download_path=self.current_data_dir
                ))
                return True
                
            raise FileNotFoundError(response.DOWNLOAD_DATASET_FAILED.value.format(dataset_name=dataset_name, error="downloaded files are missing or empty."))
    
        except Exception as e:
            logger.error(response.DOWNLOAD_DATASET_FAILED.value.format(dataset_name=dataset_name, error=str(e)))
            sys.exit(1)