import os,sys
import pandas as pd
sys.path.append(os.getcwd())
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object
import numpy as np

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            logging.info(f'{features}  Before')
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred

        except Exception as e:
            logging.info('Exception Occurred at prediction_pipeline : predict')
            raise CustomException(e,sys)
class CustomData:
    def __init__(self,v1:float,v2:float,v3:float,v4:float,v5:float,v6:float,v7:float,v8:float):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.v5 = v5
        self.v6 = v6
        self.v7 = v7
        self.v8 = v8

    def get_data_as_dataframe(self):
        try:
            input_df = np.array([[self.v1,self.v2,self.v3,self.v4,self.v5,self.v6,self.v7,self.v8]])
            logging.info('Input Data Gathered')
            return input_df
        except Exception as e:
            logging.info('Exception Occurred at Prediction pipeline : get_data_as_dataframe')
            raise CustomException(e,sys)
