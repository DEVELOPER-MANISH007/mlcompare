"""
Utility functions for MLCompare.
"""

import pandas as pd

from sklearn.model_selection import train_test_split


# Validate Inputs()
## ----------------------------------------------------------------------------
def validate_inputs(data, target=None):
    """
    Validate input dataset and target values.

    This function supports two calling patterns:
    - validate_inputs(data_frame, target_column_name)
    - validate_inputs(features, target_series)
    """

    if isinstance(data, pd.DataFrame) and isinstance(target, str):
        if data.empty:
            raise ValueError("Input DataFrame is empty.")

        if target not in data.columns:
            raise ValueError(f"Target column '{target}' not found.")

        if data[target].isnull().all():
            raise ValueError("Target column contains only missing values.")

        return data.drop(columns=[target]), data[target]

    if target is None:
        raise TypeError("target must be provided.")

    X = data
    y = pd.Series(target)

    if isinstance(X, pd.DataFrame) and X.empty:
        raise ValueError("Input DataFrame is empty.")

    if y.empty:
        raise ValueError("Target values are empty.")

    if y.isnull().all():
        raise ValueError("Target column contains only missing values.")

    return X, y


# 2️⃣ detect_problem()
def detect_problem(y):
    """
    Automatically detect classification or regression.
    """

    if (
        y.dtype == "object"
        or str(y.dtype) == "category"
        or y.dtype == "bool"
    ):
        return "classification"

    elif pd.api.types.is_integer_dtype(y):
        if y.nunique() <= 20:
            return "classification"
        return "regression"

    elif pd.api.types.is_float_dtype(y):
        return "regression"

    else:
        raise ValueError("Unable to detect problem type.")


# 3️⃣ split_data()
def split_data(
    data,
    target=None,
    problem_type=None,
    test_size=0.2,
    random_state=42,
):
    """
    Split dataset into train and test sets.

    Supports both the convenience form with a DataFrame and target column name,
    and the direct form with features X and target values y.
    """

    if isinstance(problem_type, str):
        X = data.drop(columns=[target])
        y = data[target]
        split_test_size = test_size
        split_random_state = random_state
        detected_problem = problem_type
    else:
        X = data
        y = target
        split_test_size = problem_type
        split_random_state = test_size
        detected_problem = detect_problem(y)

    stratify = y if detected_problem == "classification" else None

    try:
        return train_test_split(
            X,
            y,
            test_size=split_test_size,
            random_state=split_random_state,
            stratify=stratify,
        )
    except ValueError as exc:
        if stratify is not None and "least populated classes" in str(exc):
            return train_test_split(
                X,
                y,
                test_size=split_test_size,
                random_state=split_random_state,
                stratify=None,
            )
        raise