import os
import sys
import dill # for serializing objects to files
import json

from sklearn.metrics import r2_score

import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logger


def save_object(file_path, obj):
    """Saves an object to a file."""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)
    
def save_report_readable(file_path, obj):
    """Saves a dictionary report to a file in a readable format."""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(obj, f, indent=4, ensure_ascii=False)
    except Exception as e:
        raise CustomException(e, sys)

    

def evaluate_model(X_train, y_train, X_test, y_test, models):
    """Evaluates models and returns a report."""

    logger.info("Entered model evaluation method or component!")
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            logger.info(f"Training model: {model}")

            model.fit(X_train, y_train)
            logger.info(f"Model {model} trained successfully!")

            y_train_pred = model.predict(X_train)
            logger.info(f"{model} predictions for train set completed!")

            y_test_pred = model.predict(X_test)
            logger.info(f"{model} predictions for test set completed!")

            train_model_score = r2_score(y_train, y_train_pred)
            logger.info(f"R2 score for train set: {train_model_score}")

            test_model_score = r2_score(y_test, y_test_pred)
            logger.info(f"R2 score for test set: {test_model_score}")

            report[list(models.keys())[i]] = (train_model_score, test_model_score)
            logger.info(f"Model {model} evaluation completed!")

        return report
    except Exception as e:
        raise CustomException(e, sys)