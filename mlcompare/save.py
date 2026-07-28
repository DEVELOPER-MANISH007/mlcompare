"""
Save and load MLCompare models.
"""

import joblib


def save_model(model: object, path: str) -> None:
    """
    Save a trained machine learning model to disk.

    Parameters
    ----------
    model : object
        Trained machine learning model.

    path : str
        File path where the model will be saved.

    Raises
    ------
    ValueError
        If the model is None.
    """

    if model is None:
        raise ValueError(
            "No trained model found. Run compare() before saving."
        )

    joblib.dump(model, path)


def load_model(path: str) -> object:
    """
    Load a trained machine learning model from disk.

    Parameters
    ----------
    path : str
        Path to the saved model.

    Returns
    -------
    object
        Loaded machine learning model.
    """

    return joblib.load(path)