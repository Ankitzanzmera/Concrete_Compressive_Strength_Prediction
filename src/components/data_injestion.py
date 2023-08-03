import sys
import os
import pandas as pd
from dataclasses import dataclass
sys.path.append(os.getcwd())
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split


@dataclass
class DataInjestionconfig:
    raw_data_path = os.path.join('artifacts','raw.csv')
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.injestion_config = DataInjestionconfig()

    def initiate_data_injestion(self):
        logging.info('Data Injestion Started')

        try:
            df = pd.read_csv(os.path.join('notebooks\data','concrete_data.csv'))
            logging.info('Dataset Read as Pandas Data Frame')

            os.makedirs(os.path.dirname(self.injestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.injestion_config.raw_data_path,index = False)

            logging.info('reached Train Test Split')
            train_set,test_set = train_test_split(df,test_size=0.3,random_state=42)

            train_set.to_csv(self.injestion_config.train_data_path)
            test_set.to_csv(self.injestion_config.test_data_path)
            logging.info('Train Test Split Done')
            logging.info('Whole Data Injestion is Done...')

            return (
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path
            )

        except Exception as e:
            logging.info('Error Occured in Data Injestion Config')
            raise CustomException(e,sys)
