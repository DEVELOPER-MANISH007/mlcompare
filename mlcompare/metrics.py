"""
Evaluation metrics for MLCompare.
"""

import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

def compute_metrics(problem_type, y_true, y_pred):
    """
    Compute evaluation metrics.

    Parameters
    ----------
    problem_type : str
        Either 'classification' or 'regression'.

    y_true : array-like
        Actual target values.

    y_pred : array-like
        Predicted target values.

    Returns
    -------
    dict
        Dictionary containing evaluation metrics.
    """

    if problem_type == "classification":

        return {

            "Accuracy": accuracy_score(y_true, y_pred),

            "Precision": precision_score(
                y_true,
                y_pred,
                average="weighted",
                zero_division=0,
            ),

            "Recall": recall_score(
                y_true,
                y_pred,
                average="weighted",
                zero_division=0,
            ),

            "F1 Score": f1_score(
                y_true,
                y_pred,
                average="weighted",
                zero_division=0,
            ),
        }
    elif problem_type == "regression":

        mse = mean_squared_error(y_true, y_pred)

        return {

            "MAE": mean_absolute_error(y_true, y_pred),

            "MSE": mse,

            "RMSE": np.sqrt(mse),

            "R2 Score": r2_score(y_true, y_pred),
        }
    else:

        raise ValueError(
            "Problem type must be 'classification' or 'regression'."
        )