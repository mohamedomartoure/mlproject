import sys
import logger
import logging

def error_message_detail(error, error_detail: sys):
    """error_message_detail function to get the file name and line number where exception occurred
    Inputs:
        error: Exception object
        error_detail: sys module
    returns: 
        formatted error message
    """

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    """Custom Exception class that extends the base Exception class.
    Inputs:
        error: Exception object
        error_detail: sys module
    returns: 
        log file with error details
        formatted error message
    """

    def __init__(self, error_message, error_detail: sys):
        
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

        logger.logger.exception(self.error_message)

    def __str__(self):
        return self.error_message
    

# Test the CustomException class and store the log using logging module
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException(e, sys)
