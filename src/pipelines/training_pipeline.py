import sys
import os
sys.path.append(os.getcwd())
from src.logger import logging
from src.exception import CustomException
from src.components.data_injestion import DataInjestion

if __name__ == '__main__':
    obj = DataInjestion()
    train_data_path,test_data_path = obj.initiate_data_injestion()

    print(train_data_path,test_data_path)