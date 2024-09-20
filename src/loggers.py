import logging
from datetime import datetime
import os

LOG_FILE=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log "
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_file=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[%(asctime)s ]%(lineno)-15s %(user)-8s %(message)s",
    level=logging.INFO

)



