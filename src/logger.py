import logging
import os
from datetime import datetime

LOG_DIR_NAME = f"{datetime.now().strftime('%m_%d_%Y')}"
log_dir_path = os.path.join(os.getcwd(), 'logs' , LOG_DIR_NAME)
os.makedirs(log_dir_path , exist_ok=True)

file_name = f"{datetime.now().strftime('Time_%H-%M-%S.log')}"
LOG_FILE_PATH = os.path.join(log_dir_path , file_name)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)