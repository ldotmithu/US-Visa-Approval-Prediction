from mlProject import logging
from mlProject.config.configuration import *
import zipfile,os
import urllib.request as request


class DataIngestion:
    def __init__(self, config = DataIngestionConfig) -> None:
         self.config = config
         
    def download_file(self):
        if not os.path.exists(self.config.local_data_path): 
            request.urlretrieve(self.config.URL, 
                                self.config.local_data_path)
            
            logging.info('Zip file Downloaded')
            
        else: 
            logging.info('File Already Exists')  
            
    def Extract_data(self):
        unzip_path=self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_path , 'r') as f :
            f.extractall(unzip_path)
            logging.info('File Exreacted')                       