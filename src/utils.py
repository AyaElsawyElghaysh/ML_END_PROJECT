import pandas as pd 
import numpy as np 
import os 
import sys
from src.execption import MyCustomException
from sklearn.metrics import r2_score
import dill
import pickle
from src.loggers import logging

''' this file for any common functionalites over app '''


def save_preprocesing_pipeline_as_pk(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise MyCustomException(e,sys)



def evaluate(xtrain,ytrain,xtest,ytest,models):
    '''this function for evaluating each model ...'''
                               
        # models={
        #    'lr' : LinearRegression(),
        #    'adaboost' : AdaBoostRegressor(),
        #    'gb':GradientBoostingRegressor()
        # }
    models_reports={}
    for model_name,model_obj in models.items():
        
        model_obj.fit(xtrain,ytrain)

        y_train_predict=model_obj.predict(xtrain)
        y_test_predict=model_obj.predict(xtest)

        train_model_score=r2_score(ytrain,y_train_predict)
        test_model_score=r2_score(ytest,y_test_predict)

        models_reports[model_name]={'train_model_score':train_model_score,'test_model_score':test_model_score}



    return models_reports



def save_model_as_pkl(model_path,model_obj):
    try:
        dir_path= os.path.dirname(model_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(model_path, "wb") as file_obj:
            pickle.dump(model_obj, file_obj)



    except Exception as e:
        raise MyCustomException(e,sys)


