import logging
import os
from datetime import datetime
import exception

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

# log exception info
# def get_logger(name: str = None):
#     return logging.getLogger(name)

logger = logging.getLogger(None)

if __name__ == "__main__":
    logging.info("Logging setup complete. Log file created at: %s", LOG_FILE_PATH)
  

