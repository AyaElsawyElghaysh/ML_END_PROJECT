import numpy as np 
import sys
from sklearn.compose import ColumnTransformer
import pandas as pd
import os 
from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, RobustScaler, StandardScaler
from src.loggers import logging 
from src.execption import MyCustomException
import category_encoders as ce
from src.utils import save_preprocesing_pipeline_as_pk

@dataclass
class DataTransformationConfig:
    preprocess_file_path: str = os.path.join('artifact',"proprocessor.pkl")

class DataTransformation:
    def __init__(self) -> None:
        self.data_transformation_path = DataTransformationConfig()

    def get_data_transformation(self):
        try:
            logging.info("Transformation started..")
            numerical_features = ['DIFF_STD_STA']  # Uncomment this if used
            categorical_features = ['DEPSTN', 'ARRSTN', 'STATUS']

          #   num_pipeline = Pipeline(
          #       steps=[
          #           ('scaler', StandardScaler()),
          #       ]
          #   )

            cat_pipeline = Pipeline(
                steps=[
                    ('cat', ce.TargetEncoder())
                    , ('scaler', StandardScaler())
                ]
            )

            logging.info("Transformation has been done on both numerical and categorical")
            processor = ColumnTransformer(
                transformers=[
                    # ('numerical', num_pipeline, numerical_features),  # Uncomment if used
                    ('categorical', cat_pipeline, categorical_features)
                ]
            )

            logging.info("Triggering the pipeline has been done on both numerical and categorical")
            return processor
        except Exception as e:
            raise MyCustomException(e, sys)

    def initiate_data_transformation(self,train_path,test_path):

               try:
                    train_df=pd.read_csv(train_path)
                    test_df=pd.read_csv(test_path)
                    print("helllo")
                    logging.info("Read train and test data completed")

                    logging.info("Obtaining preprocessing object")

                    preprocessing_obj=self.get_data_transformation()

                    target_column_name="target"
                

                    input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
                    target_feature_train_df=train_df[target_column_name]

                    input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
                    target_feature_test_df=test_df[target_column_name]

                    logging.info(
                         f"Applying preprocessing object on training dataframe and testing dataframe."
                    )

                    input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df,target_feature_train_df)
                    input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

                    train_arr = np.c_[
                         input_feature_train_arr, np.array(target_feature_train_df)
                    ]
                    test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

                    logging.info(f"Saved preprocessing object.")

                    save_preprocesing_pipeline_as_pk(

                         file_path=self.data_transformation_path.preprocess_file_path,
                         obj=preprocessing_obj
                         
                    

                    )

                    return (
                         train_arr,
                         test_arr,
                         self.data_transformation_path.preprocess_file_path,
                    )
               except Exception as e:
                    raise MyCustomException(e,sys)
