import pandas as pd
from sqlalchemy import create_engine
from src.utils.logger_config import logger
from src.utils.responses import ResponseStatus as response

class DatabaseLoader:
    def __init__(self, user, password, db_name, host="localhost", port="5432"):
        
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
      
        connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        self.engine = create_engine(connection_string)
        logger.info(response.DB_LOADER_CONNECTION_ESTABLISHED.value.format(db_name=self.db_name))

    
    def upload_to_staging(self, df, table_name="stg_logistics"):
        try:
            logger.info("⏳ Uploading data to the staging table...")
            

            with self.engine.begin() as connection:
                df.to_sql(table_name, con=connection, if_exists="replace", index=False)
            
            logger.info(f"✅ SUCCESS: Processed data uploaded successfully to table [{table_name}]!")
            
        except Exception as e:
            logger.error(f"❌ CRITICAL DATABASE ERROR: {str(e)}")