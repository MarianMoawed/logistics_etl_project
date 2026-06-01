from src.utils.logger_config import logger
from config.config import KAGGLE_DATASET_NAME
from src.utils.responses import ResponseStatus as response
from src.ingestion.kaggle_boostraper import KaggleBootstrapper
from src.ingestion.kaggle_extractor import KaggleExtractor



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

if __name__ == "__main__":
    run_pipeline()