from enum import Enum


class ResponseStatus(Enum):

    AUTH_START = "starting kaggle apt authentication process."
    AUTH_SUCCESS = "kaggle api authentication successful!."
    AUTH_FAILED = "authentication failed!.error details: {error}."

    CREDINTIALS_MISSING = "kaggle credentials file not found at{path}." \
    "please create it with your Kaggle API credentials."