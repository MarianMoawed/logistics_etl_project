from enum import Enum


class ResponseStatus(Enum):

    AUTH_START = "starting kaggle apt authentication process."
    AUTH_SUCCESS = "kaggle api authentication successful!."
    AUTH_FAILED = "authentication failed!.error details: {error}."

    CREDINTIALS_MISSING = "kaggle credentials file not found at{path}." \
    "please create it with your Kaggle API credentials."

    DOWNLOAD_DATASET_START = "starting download of dataset: {dataset_name}."
    DOWNLOAD_DATASET_SUCCESS = "dataset {dataset_name} downloaded successfully to {download_path}."
    DOWNLOAD_DATASET_FAILED = "failed to download dataset {dataset_name}. error details: {error}."

    PIPLINE_START = "starting the logistics ETL pipeline execution."
    PIPELINE_INIT_ENVIRONMENT = "initializing kaggle environment for dataset extraction."
    PIPELINE_START_EXTRACTION = "starting dataset extraction process."
    PIPELINE_KAGGLE_EXTRACTION_SUCCESS = "dataset extraction from kaggle completed successfully."
    PIPELINE_KAGGLE_EXTRACTION_FAILED = "failed to extract dataset from kaggle,due to an unhandeled error. error details: {error}."