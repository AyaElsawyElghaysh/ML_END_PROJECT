import os
import logging
from datetime import datetime

# Ensure the logs directory exists
log_directory = os.path.join(os.getcwd(), "logs")
os.makedirs(log_directory, exist_ok=True)  # Creates the directory if it doesn't exist

# Set up logging
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
log_path = os.path.join(log_directory, LOG_FILE)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

# if __name__ == "__main__":
#     logging.info("LOGGING HAS STARTED")
