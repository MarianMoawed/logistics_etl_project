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

    SHIFTING_NO_DATE_COLUMNS = "no date columns provided for shifting, returning original DataFrame."
    SHIFTING_REFERENCE_COLUMN_HAS_NO_VALID_DATES = "reference column '{reference_column}' has no valid date values. cannot determine max year for shifting."
    SHIFTING_YEARS = "shifting years in columns {date_columns} by {years_to_add} years to align with 2026."
    SHIFTING_REFERENCE_COLUMN_NOT_FOUND = "reference column '{reference_column}' not found in DataFrame. cannot determine max year for shifting."
    SHIFTED_YEARS_IN_COLUMN = "shifted years in column '{col}' by {years_to_add} years."
    SHIFTING_COMPLETED = "year shifting completed for all specified date columns."


    TRANSFORM_DROP_COLUMNS = "dropping columns: {columns}."
    TRANSFORM_NO_COLUMNS_TO_RENAME = "no columns to rename, returning original DataFrame."
    TRANSFORM_RENAMING_COLUMNS = "renaming columns: {columns_mapping}."
    TRANSFORM_NO_COLUMNS_TO_CONVERT_TO_DATETIME = "no columns to convert to datetime, returning original DataFrame."
    TRANSFORM_CONVETED_COLUMN_TO_DATETIME = "converted column '{col}' to datetime."
    TRANSFORM_COLUMN_NOT_FOUND_IN_DF = "column '{col}' not found in DataFrame, skipping conversion."

    DB_LOADER_CONNECTION_ESTABLISHED = "database connection established successfully to {db_name}."
    DB_LOADER_DATA_UPLOADED = "data uploaded successfully to the staging table in the database {db_name}."
    DB_LOADER_UPLOAD_FAILED = "failed to upload data to the staging table in the database {db_name}. error details: {error}."
    
    PIPLINE_START = "starting the logistics ETL pipeline execution."
    PIPELINE_INIT_ENVIRONMENT = "initializing kaggle environment for dataset extraction."
    PIPELINE_START_EXTRACTION = "starting dataset extraction process."
    PIPELINE_KAGGLE_EXTRACTION_SUCCESS = "dataset extraction from kaggle completed successfully."
    PIPELINE_KAGGLE_EXTRACTION_FAILED = "failed to extract dataset from kaggle,due to an unhandeled error. error details: {error}."
    
    PIPELINE_READING_RAW_DATA = "reading raw data from: {raw_data_path}."
    PIPELINE_RAW_DATA_READ_SUCCESS = "raw data read successfully with shape: {shape}."
    PIPELINE_START_DATESHIFTING = "starting data dateshifting to align with 2026."
    PIPELINE_START_CLEANING_TRANSFORMATION = "starting data cleaning and transformation."
    PIPELINE_COLUMNS_DROPPED = "columns dropped successfully, new shape: {shape}."
    PIPELINE_COLUMNS_RENAMED = "columns renamed successfully, new shape: {shape}."
    PIPELINE_DATE_COLUMNS_CONVERTED = "date columns converted to datetime successfully, new shape: {shape}."
    PIPELINE_PROCESSED_DATA_SAVED = "processed data saved successfully to: {processed_data_path}."
    PIPELINE_UPLOAD_TO_STAGING = "uploading processed data to the staging table in the database."
    PIPELINE_UPLOAD_SUCCESS = "processed data uploaded successfully to the staging table in the database."
    PIPELINE_UPLOAD_FAILED = "failed to upload processed data to the staging table in the database. error details: {error}."