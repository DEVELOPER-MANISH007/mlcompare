"""
All machine learning models used in MLCompare.
"""

from sklearn.linear_model import (
    LogisticRegression,
    LinearRegression,
    Ridge,
    Lasso,
    ElasticNet,
)

from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC

from sklearn.tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
)

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor,
    AdaBoostClassifier,
    GradientBoostingClassifier,
    GradientBoostingRegressor,
    ExtraTreesClassifier,
    ExtraTreesRegressor,
)

RANDOM_STATE = 42


# ----------------------------------------------------------------------------  

# Classification models

classification_models = {

    "Logistic Regression": LogisticRegression(random_state=RANDOM_STATE),

    "KNN": KNeighborsClassifier(),

    "SVM": SVC(random_state=RANDOM_STATE),

    "Decision Tree": DecisionTreeClassifier(random_state=RANDOM_STATE),

    "Random Forest": RandomForestClassifier(random_state=RANDOM_STATE),

    "AdaBoost": AdaBoostClassifier(random_state=RANDOM_STATE),

    "Gradient Boosting": GradientBoostingClassifier(random_state=RANDOM_STATE),

    "Extra Trees": ExtraTreesClassifier(random_state=RANDOM_STATE),

}

# ----------------------------------------------------------------------------  

# Regression models

regression_models = {

    "Linear Regression": LinearRegression(),

    "Ridge": Ridge(),

    "Lasso": Lasso(),

    "ElasticNet": ElasticNet(),

    "Decision Tree": DecisionTreeRegressor(random_state=RANDOM_STATE),

    "Random Forest": RandomForestRegressor(random_state=RANDOM_STATE),

    "Gradient Boosting": GradientBoostingRegressor(random_state=RANDOM_STATE),

    "Extra Trees": ExtraTreesRegressor(random_state=RANDOM_STATE),

}


# ----------------------------------------------------------------------------  
# Get models
def get_models(problem_type: str):
    """
    Return machine learning models based on problem type.

    Parameters
    ----------
    problem_type : str
        Either 'classification' or 'regression'.

    Returns
    -------
    dict
        Dictionary containing model names and model objects.
    """

    if problem_type == "classification":
        return classification_models

    elif problem_type == "regression":
        return regression_models

    else:
        raise ValueError(
            "Problem type must be 'classification' or 'regression'."
        )

