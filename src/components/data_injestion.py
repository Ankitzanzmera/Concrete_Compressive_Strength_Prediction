import sys
import os
import pandas as pd
from dataclasses import dataclass
sys.path.append(os.getcwd())
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split

@dataclass
class DataInjestionConfig:
    raw_data_path = os.path.join('artifacts','raw.csv')
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')

class DataInjestion:
    def __init__(self):
        self.injestion_config = DataInjestionConfig()

    def initiate_data_injestion(self):
        try:
            df = pd.read_csv(os.path.join('notebooks\data','concrete_data.csv'))
            logging.info('Dataset load successfully')
            os.makedirs(os.path.dirname(self.injestion_config.raw_data_path,),exist_ok=True)
            df.to_csv(self.injestion_config.raw_data_path,index = False)

            train_data,test_data = train_test_split(df,test_size=0.3,random_state=42)
            logging.info('Train Test Split Done ')

            train_data.to_csv(self.injestion_config.train_data_path,index = False)
            test_data.to_csv(self.injestion_config.test_data_path,index = False)

            logging.info('All Dataset are stored in Artifacts Folder')
            logging.info('Data Injestion is Done')

            return (
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path
            )


        except Exception as e:
            logging.info('Exception Occurred at Data Injestion file')
            raise CustomException(e,sys)