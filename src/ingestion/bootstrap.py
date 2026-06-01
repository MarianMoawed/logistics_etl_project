import os
from abc import ABC, abstractmethod
import config.config as config




class BaseBootstrapper:
    '''Handles the initial setup for Kaggle API authentication and environment preparation.'''

    def __init__(self):
        pass

    
    @abstractmethod
    def setup_environment(self):
        pass


