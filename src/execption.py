import sys
from src.loggers import logging

import sys

def get_error_messages(error, error_details: sys):
    _, _, file_exc = error_details.exc_info()
    file_name = file_exc.tb_frame.f_code.co_filename
    error_message = f'The error occurred in file {file_name} at line number {file_exc.tb_lineno}. Error message: {str(error)}'
    return error_message

class MyCustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = get_error_messages(error_message, error_details)

    def __str__(self) -> str:
        return self.error_message




#test this script
# if __name__ == "__main__":
#     try:
#        a=1/0
       
#     except Exception as e:
#        logging.info("devision by zero not allowed")
#        raise MyCustomException(e,sys)
       

       
   