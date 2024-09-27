import pandas as pd
from src.components import dataTransformation
import numpy as np 
import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor,RandomForestClassifier
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

from src.execption import MyCustomException
from src.loggers import logging

from src.utils import save_preprocesing_pipeline_as_pk,save_model_as_pkl
from src.utils import evaluate
@dataclass
class ModelTrainConfig :
   model_path :str = os.path.join("artifact","model.pkl")



class ModelTraining :
   
   def __init__ (self):
      self.model_path=ModelTrainConfig()

   def init_train_model(self,xtrain_array,test_array,preprocessor_path=None):
      try:
        logging.info("init model training....")
        x_train,ytrain,x_test,y_test=(xtrain_array[:,:-1],
                                      xtrain_array[:,-1],
                                      test_array[:,:-1],
                                      test_array[:,-1])
        models={
           'lr' : LinearRegression(),
           'adaboost' : AdaBoostRegressor(),
           'gb':GradientBoostingRegressor()
        }
        models_reports:dict = evaluate(x_train,ytrain,
                                       x_test,y_test,models)
        # models_reports[model_name]={'train_model_score':train_model_score,
        #'test_model_score':test_model_score}

        best_model, best_score = max(models_reports.items(), key=lambda item: item[1]['test_model_score'])

        print(f"Best Model: {best_model}, Best Score: {best_score['test_model_score']}")
       
        save_model_as_pkl(self.model_path.model_path,best_model)
      except Exception as e:
         raise MyCustomException(e,sys)

   

