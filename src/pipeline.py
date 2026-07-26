import pandas as pd
import os
from dotenv import load_dotenv

from src.utils.logger_config import logger
from config.config import KAGGLE_DATASET_NAME
from src.utils.responses import ResponseStatus as response
from src.ingestion.kaggle_boostraper import KaggleBootstrapper
from src.ingestion.kaggle_extractor import KaggleExtractor
from src.pipelines.time_shifter import shift_years_to_2026
from src.pipelines.transform_cleaner import DataCleaner
from src.pipelines.db_loader import DatabaseLoader

current_dir = os.path.dirname(os.path.abspath(__file__)) # ده فولدر src
parent_dir = os.path.dirname(current_dir)                # ده الفولدر الرئيسي للمشروع
dotenv_path = os.path.join(parent_dir, '.env')

load_dotenv(dotenv_path=dotenv_path)

def run_pipeline():
    logger.info(response.PIPLINE_START.value)

    try:
        logger.info(response.PIPELINE_INIT_ENVIRONMENT.value)

        kaggle_bootstrapper = KaggleBootstrapper()
        kaggle_api = kaggle_bootstrapper.setup_environment()


        logger.info(response.PIPELINE_START_EXTRACTION.value)
        kaggle_extractor = KaggleExtractor(kaggle_api)

        dataset_name = KAGGLE_DATASET_NAME  
        success = kaggle_extractor.download_dataset(dataset_name)
        if success:
            logger.info(response.PIPELINE_KAGGLE_EXTRACTION_SUCCESS.value)
    except Exception as e:
        logger.critical(response.PIPELINE_KAGGLE_EXTRACTION_FAILED.value.format(error=str(e)))

    
    raw_data_path = 'data/raw/2026-06-03/DataCoSupplyChainDataset.csv'
    processed_data_path = 'data/processed/2026-06-03/processed_data.csv'

    logger.info(response.PIPELINE_READING_RAW_DATA.value.format(raw_data_path=raw_data_path))
    raw_df = pd.read_csv(raw_data_path,encoding='latin-1')
    logger.info(response.PIPELINE_RAW_DATA_READ_SUCCESS.value.format(shape=raw_df.shape))

    logger.info(response.PIPELINE_START_DATESHIFTING.value)
    shifted_df = shift_years_to_2026(
        raw_df,
        date_columns=['order date (DateOrders)', 'shipping date (DateOrders)'],
        reference_column='order date (DateOrders)'
    )
    logger.info(response.PIPELINE_START_CLEANING_TRANSFORMATION.value)

    cleaner = DataCleaner()

    columns_to_drop = [
        'Customer Lname', 'Customer Fname', 'Customer Email',
        'Customer Password', 'Customer Zipcode',
        'Product Description', 'Product Status', 'Latitude',
        'Longitude', 'Order Zipcode', 'Benefit per order'
    ]
    cleaned_df = cleaner.drop_columns(shifted_df, columns=columns_to_drop)
    logger.info(response.PIPELINE_COLUMNS_DROPPED.value.format(shape=cleaned_df.shape))

    columns_to_rename = {
        'Order Item Total': 'Net Sales',
        'Sales': 'Gross Sales',
        'Order Profit Per Order': 'Profit Per Order',
        'order date (DateOrders)': 'Order Date',
        'shipping date (DateOrders)': 'Ship Date'
    }
    renamed_df = cleaner.rename_columns(cleaned_df, columns_mapping=columns_to_rename)
    logger.info(response.PIPELINE_COLUMNS_RENAMED.value.format(shape=renamed_df.shape))

    date_columns = ['Order Date', 'Ship Date']
    final_df = cleaner.convert_to_datetime(renamed_df, date_columns=date_columns)
    logger.info(response.PIPELINE_DATE_COLUMNS_CONVERTED.value.format(shape=final_df.shape))

    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)
    final_df.to_csv(processed_data_path, index=False)
    logger.info(response.PIPELINE_PROCESSED_DATA_SAVED.value.format(processed_data_path=processed_data_path))

    logger.info(response.PIPELINE_UPLOAD_TO_STAGING.value)
    try:
        loader = DatabaseLoader(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            db_name=os.getenv('DB_NAME'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        
        loader.upload_to_staging(final_df)
        logger.info(response.PIPELINE_UPLOAD_SUCCESS.value)
    except Exception as e:
        logger.error(response.PIPELINE_UPLOAD_FAILED.value.format(error=str(e)))
   


if __name__ == '__main__':
    run_pipeline()