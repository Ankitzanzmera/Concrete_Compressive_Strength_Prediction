import pickle
import sys
import os
sys.path.append(os.getcwd())
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

def cate_num_feature():
    try:
        logging.info('Separation of Categorical and numerical Columns are initiated')
        df = pd.read_csv(os.path.join('notebooks\data','concrete_data.csv'))
        cate_features = df.columns[df.dtypes == 'object']
        num_features = df.columns[df.dtypes != 'object']

        return cate_features,num_features

    except Exception as e:
        logging.info('Exception in the utils file and at cate_num_feature')
        raise CustomException(e,sys)

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        logging.info('Exception occurred at utils : save_object')
        raise CustomException(e,sys)


def evaluate_model(y_test,y_pred):
    try:
        report = {}
        report['Mean_squared_error'] = mean_squared_error(y_test,y_pred)
        report['Mean_Absolute_error'] = mean_absolute_error(y_test, y_pred)
        report['R2_Score'] = r2_score(y_test, y_pred)
        return report
    except Exception as e:
        logging.info('Error occurred at utils.py : evaluate_model')
        raise CustomException(e,sys)

def load_object(path):
    try:
        with open(path,'rb') as file_obj:
            return pickle.load(e,sys)
    except Exception as e:
        logging.info('Exception occurred during loading a Object')
        raise CustomException(e,sys)



if __name__=="__main__":
    logging.info('Code Run start')
    print(cate_num_feature())

