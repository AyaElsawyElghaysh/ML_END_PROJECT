from dataclasses import dataclass
from src.loggers import logging
from src.execption import MyCustomException
import pandas as pd 
from sklearn.model_selection import train_test_split
import os
import yaml
import sys
from src.components.dataTransformation import DataTransformation
from src.components.modelTranier import ModelTraining
@dataclass
class DataLoadingConfig:
    """
    this class for creating three folders for train and test,raw_data
    """
    train_data_path:str=os.path.join("artifact","train.csv")
    test_data_path:str=os.path.join("artifact","test.csv")
    raw_data:str=os.path.join("artifact","raw.csv")



class DataLoading:
    """
      this class for loading the data into their folders created by DataLoadingConfig 
      and split the data into train and testing
    """
    def __init__(self):

         self.load_init=DataLoadingConfig()
        
    def load_data(self):
        try :
            logging.info("data is entered")
            with open ("data_paths.yaml",'r') as file:
                         data=yaml.safe_load(file)

            data_=data['train_path']
            
            df=pd.read_csv(data_)
          
            logging.info("reading the dataset from dataframe")
            os.makedirs(os.path.dirname(self.load_init.train_data_path),exist_ok=True)
            df.to_csv(self.load_init.raw_data)
            logging.info("train_test_split initialized .....")
            X_train,x_test=train_test_split(df,test_size=0.2,random_state=42)
            X_train.to_csv(self.load_init.train_data_path,index=False,header=True)
            x_test.to_csv(self.load_init.test_data_path,index=False,header=True)
            return (self.load_init.train_data_path,
                    self.load_init.test_data_path)





        except Exception as e:
              raise MyCustomException(e,sys)


if __name__=='__main__':
      data=DataLoading()

      xtrain,xtest= data.load_data()
      data_transformation_obj=DataTransformation()
      train_arr, test_arr,_= data_transformation_obj.initiate_data_transformation(xtrain,xtest)
      model_train=ModelTraining()
      model_train.init_train_model(train_arr,test_arr)
      

      
    
