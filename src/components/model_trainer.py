import os
import sys
sys.path.append(os.getcwd())
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from xgboost import XGBRegressor
from src.utils import save_object,evaluate_model


@dataclass
class ModelTrainerConfig:
    model_pickle_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    try:
        def __init__(self):
            self.model_trainer_config_obj = ModelTrainerConfig()

        def initiate_model_training(self, X_train, X_test, y_train, y_test):
            model = XGBRegressor()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            model_report: dict = evaluate_model(y_test, y_pred)
            logging.info(f'Model Report : {model_report}')

            save_object(
                file_path=self.model_trainer_config_obj.model_pickle_file_path,
                obj=model
            )

            logging.info('Model Pickle File is saved')

    except Exception as e:
        logging.info('Error Occurred at Model_trainer : initiate_model_trainer')
        raise CustomException(e,sys)
