import pandas as pd 
import numpy as np 
import os 
import sys
from src.execption import MyCustomException
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


