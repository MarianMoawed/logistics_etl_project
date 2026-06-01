import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_FILE_PATH = os.path.join(BASE_DIR, "logs","pipeline.log" )

KAGGLE_DATASET_NAME = "harshsingh2209/supply-chain-analysis"

def get_data_dir(source_name:str) -> str:

    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(BASE_DIR, "data", today)



