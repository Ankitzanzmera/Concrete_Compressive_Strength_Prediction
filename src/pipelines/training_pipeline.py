import sys
import os
sys.path.append(os.getcwd())
from src.logger import logging
from src.exception import CustomException
from src.components.data_injestion import DataInjestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == '__main__':
    try:
        obj = DataInjestion()
        train_data_path,test_data_path = obj.initiate_data_injestion()
        logging.info('Step 1 : Data Injestion Completed')


        data_transformation = DataTransformation()
        X_train_preprocessed , X_test_preprocessed , y_train ,y_test = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        logging.info('Step 2 :Data Transformation Completed')

        model_trainer = ModelTrainer()
        model_trainer.initiate_model_training(X_train_preprocessed , X_test_preprocessed , y_train ,y_test)
        logging.info('Step 3 :Model Training is Done')



    except Exception as e:
        logging.info('Error Occurred at training pipeline file')
        raise CustomException(e,sys)
