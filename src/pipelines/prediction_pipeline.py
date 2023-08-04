import os,sys
import pandas as pd
sys.path.append(os.getcwd())
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

        except Exception as e:
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
            custom_data_input = {
                'cement':self.v1,
                'blast_furnace_slag':self.v2,
                'fly_ash':self.v3,
                'water':self.v4,
                'superplasticizer':self.v5,
                'coarse_aggregate':self.v6,
                'fine_aggregate':self.v7,
                'age':self.v8
            }
            input_df = pd.DataFrame(custom_data_input)
            logging.info('Input Data Gathered')
            return input_df
        except Exception as e:
            logging.info('Exception Occurred at Prediction pipeline : get_data_as_dataframe')
            raise CustomException(e,sys)
