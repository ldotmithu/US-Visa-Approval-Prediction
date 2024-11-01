from mlProject import logging
from mlProject.entity.config_entity import *
from mlProject.utils.common import read_yaml,create_directories
from mlProject.constants import *

class ConfigManager:
    def __init__(self) :
        self.config = read_yaml(CONFIG_FILE_PATH)
        self.params = read_yaml(PARAMS_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        create_directories([self.config.arifacts_root])
        
    def get_data_ingestion_config(self):
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])    

