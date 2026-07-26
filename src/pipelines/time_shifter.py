import pandas as pd
from src.utils.logger_config import logger
from src.utils.responses import ResponseStatus as response


def shift_years_to_2026(df:pd.DataFrame, date_columns:list, reference_column:str):
    if not date_columns:
        logger.info(response.SHIFTING_NO_DATE_COLUMNS.value)
        return df

    df = df.copy()

    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    if reference_column in df.columns:
        valid_reference = df[reference_column].dropna()
        if valid_reference.empty:
            logger.warning(response.SHIFTING_REFERENCE_COLUMN_NO_VALID_VALUES.value.format(reference_column=reference_column))
            return df

        max_year_in_data = valid_reference.dt.year.max()
        years_to_add = 2026 - max_year_in_data
        logger.info(response.SHIFTING_YEARS.value.format(date_columns=date_columns, years_to_add=years_to_add))
    else:
        logger.warning(response.SHIFTING_REFERENCE_COLUMN_NOT_FOUND.value.format(reference_column=reference_column))
        return df

    for col in date_columns:
        if col in df.columns:
            df[col] = df[col] + pd.DateOffset(years=years_to_add)
            logger.info(response.SHIFTED_YEARS_IN_COLUMN.value.format(col=col, years_to_add=years_to_add))

    logger.info(response.SHIFTING_COMPLETED.value)
    return df