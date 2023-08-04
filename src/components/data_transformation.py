import sys
import os
import pandas as pd
sys.path.append(os.getcwd())
from src.logger import logging
from src.exception import CustomException
from src.utils import cate_num_feature,save_object
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler

@dataclass
class DataTransformationconfig:
    preprocessor_pickle_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config_obj = DataTransformationconfig()

    def make_preprocessing_pipeline(self):
        try:
            logging.info('creating of preprocessing pipelinea are Started')
            cate_feature,num_feature = cate_num_feature()
            logging.info('Got Categorical and Numerical Columns')
            logging.info('Making of pipelines are intiated')

            cate_pipeline = Pipeline(
                steps = [
                    ('cate_imputer',SimpleImputer(strategy='most_frequent')),
                    ('OneHotEncoder',OneHotEncoder()),
                    ('cate_scaler',StandardScaler())
                ]
            )

            num_pipeline = Pipeline(
                steps=[
                    ('num_imputer',SimpleImputer(strategy='median')),
                    ('num_scaler',StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ('cate_pipeline',cate_pipeline,cate_feature),
                    ('num_pipeline',num_pipeline,num_feature)
                ]
            )
            logging.info('Pipeline Creating Completed')
            return preprocessor

        except Exception as e:
            logging.info('Exception occurred At Data Transformation file : make_preprocessing_pipeline')
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)
            logging.info('load of train and test Data is Completed')
            logging.info('obtaining make_pipeline object')

            preprocessing_obj = self.make_preprocessing_pipeline()

            target_col = 'concrete_compressive_strength'

            X_train = train_df.drop(target_col,axis = 1)
            y_train = train_df[target_col]

            X_test = test_df.drop(target_col,axis = 1)
            y_test = test_df.drop[target_col]

            logging.info('Separation of train and tests are completed')
            logging.info('Applying preprcessing pipeline on train and test data')

            X_train_preprocessed = preprocessing_obj.fit_transform(X_train)
            X_test_preprocessed = preprocessing_obj.transform(X_test)

            logging.info('preprocces Complete')

            save_object(
                file_path = self.data_transformation_config_obj.preprocessor_pickle_file_path,
                obj = preprocessing_obj
            )

            return (
                X_train_preprocessed,X_test_preprocessed,y_train,y_test
            )

        except Exception as e:
            logging.info('Exception Occurred at Data transformation file : initiate_data_transformation')
            raise CustomException(e,sys)
