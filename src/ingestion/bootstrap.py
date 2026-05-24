import os
import logging
import sys
from kaggle.api.kaggle_api_extended import KaggleApi
import config.config as config
from utils.responses import ResponseStatus as response



logger = logging.getLogger(__name__)




class KaggleBootstrapper:
    '''Handles the initial setup for Kaggle API authentication and environment preparation.'''

    def __init__(self):
        self.api = KaggleApi()

    def create_data_directory(self):

        os.makedirs(config.DATA_DIR, exist_ok=True)

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
            self.create_data_directory()
            self.secure_kaggle_credentials()
            self.authenticate_kaggle_api()
        except Exception as e:
            logger.error(response.AUTH_FAILED.value.format(error=str(e)))
            sys.exit(1)