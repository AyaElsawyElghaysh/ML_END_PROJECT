import pandas as pd 
import numpy as np 
import os 
import sys
from src.execption import MyCustomException
import dill

''' this file for any common functionalites over app '''


def save_preprocesing_pipeline_as_pk(path,processing_pipeline_object):
    try:

        dir_path=os.path.dirname(path)
        os.makedirs(path,exist_ok=True)
        with open(path,'wb') as file_path:
            dill.dump(processing_pipeline_object,file_path)
    except Exception as e:
        raise MyCustomException(e,sys)


