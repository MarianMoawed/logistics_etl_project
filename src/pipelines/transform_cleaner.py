import pandas as pd

from src.utils.logger_config import logger
from src.utils.responses import ResponseStatus as response



class DataCleaner:

    def drop_columns(self, df, columns):
        logger.info(response.PIPELINE_COLUMNS_DROPPED.value.format(shape=df.shape))
        return df.drop(columns=columns)
    
    def rename_columns(self, df, columns_mapping):
        if not columns_mapping:
            logger.info("No columns to rename, returning original DataFrame")
            return df
        logger.info(response.PIPELINE_COLUMNS_RENAMED.value.format(shape=df.shape))
        return df.rename(columns=columns_mapping)
    
    def delete_null_values(self, df, columns):
        if not columns:
            logger.info("No columns specified for dropping null values, returning original DataFrame")
            return df
        logger.info(response.PIPELINE_NULL_VALUES_DELETED.value.format(shape=df.shape))
        return df.dropna(subset=columns)
    
    def convert_to_datetime(self, df, date_columns):
        
        if not date_columns:
            logger.info("No columns to convert to datetime, returning original DataFrame")
            return df
        logger.info(response.PIPELINE_DATE_COLUMNS_CONVERTED.value.format(shape=df.shape))

        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
                logger.info(response.TRANSFORM_CONVETED_COLUMN_TO_DATETIME.value.format(col=col))
            else:
                logger.warning(response.TRANSFORM_COLUMN_NOT_FOUND_IN_DF.value.format(col=col))
        return df