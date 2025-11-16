import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor


from sklearn.metrics import r2_score

from src.logger import logger
from src.exception import CustomException
from src.utils import save_object, evaluate_model, save_report_readable

@dataclass
class ModelTrainerConfig():
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')
    report_model_file_path = os.path.join('artifacts', 'report.json')

class ModelTrainer():
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        """Trains a model using the provided training and testing data."""

        logger.info("Entered model training method or component!")
        try:
            X_train, y_train, X_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1]
            )
            logger.info("Data split into features and target variables!")

            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree Regressor": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "Gradient Boosting Regressor": GradientBoostingRegressor(),
                "Support Vector Regression": SVR(),
                "XGBoost Regressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "Ada Boost Regressor": AdaBoostRegressor()
            }
            logger.info("Models dictionary created!")

            model_report:dict = evaluate_model(X_train=X_train, 
                                               y_train=y_train, 
                                               X_test=X_test, 
                                               y_test=y_test, 
                                               models=models)
            logger.info("Model report generated!")

            save_report_readable(self.model_trainer_config.report_model_file_path, model_report)
            logger.info("Report saved!")

            best_model_score = max(sorted(list(model_report.values())[1]))
            logger.info(f"Best model score: {best_model_score}")
            
            if best_model_score < 0.6:
                raise CustomException("No best model found!")
            logger.info("Best model score is above 0.6!")

            best_model_name = list(model_report.keys())[
                list(model_report.values())[1].index(best_model_score)]
            logger.info(f"Best model name: {best_model_name}")

            best_model = models[best_model_name]
            logger.info("Best model selected!")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path, 
                obj= best_model
            )
            logger.info("Best Model Object saved!")
        
            return model_report, best_model_name, best_model_score
        
        except Exception as e:
            raise CustomException(e, sys)

