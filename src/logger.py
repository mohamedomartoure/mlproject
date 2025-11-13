import logging
import os
from datetime import datetime

# Create logs directory with current timestamp
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(log_path, exist_ok=True)

# Define the full log file path
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

# Configure logging settings and write logs to the specified file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)   

logger = logging.getLogger()
  

