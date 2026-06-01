import os
import sys
from src.utils.logger_config import logger
from src.ingestion.bootstrap import BaseBootstrapper
from kaggle.api.kaggle_api_extended import KaggleApi
import config.config as config
from src.utils.responses import ResponseStatus as response




class KaggleBootstrapper(BaseBootstrapper):

    def __init__(self):
        super().__init__()
        self.api = KaggleApi()

    

    def secure_kaggle_credentials(self):

        kaggle_json_file = os.path.expanduser('~/.kaggle/kaggle.json')

        if not os.path.exists(kaggle_json_file):

            err_msg = response.CREDINTIALS_MISSING.value.format(path=kaggle_json_file)
            raise FileNotFoundError(err_msg)
            

        os.chmod(kaggle_json_file, 0o600)


    def authenticate_kaggle_api(self):

        logger.info(response.AUTH_START.value)
        self.api.authenticate()
        logger.info (response.AUTH_SUCCESS.value)

    
    def setup_environment(self):
        try:
            
            self.secure_kaggle_credentials()
            self.authenticate_kaggle_api()
            return self.api

        except Exception as e:
            
            logger.error(response.AUTH_FAILED.value.format(error=str(e)))
            sys.exit(1)