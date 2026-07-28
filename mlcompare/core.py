"""
Main MLCompare class.
"""

import pandas as pd

from mlcompare.metrics import compute_metrics
from mlcompare.models import get_models
from mlcompare.save import save_model
from mlcompare.utils import detect_problem, split_data, validate_inputs


class MLCompare:
    """
    Compare multiple machine learning models.
    """

    def __init__(
        self,
        data: pd.DataFrame,
        target: str,
        test_size: float = 0.2,
        random_state: int = 42,
    ):
        self.data = data
        self.target = target
        self.test_size = test_size
        self.random_state = random_state

        self.problem_type = None
        self.models = None
        self.results = None
        self.best_model = None
        self.best_model_name = None
        self.trained_models = {}

    def compare(self):
        """
        Train and compare all machine learning models.
        """

        validate_inputs(self.data, self.target)

        y = self.data[self.target]
        self.problem_type = detect_problem(y)

        X_train, X_test, y_train, y_test = split_data(
            self.data,
            self.target,
            self.problem_type,
            self.test_size,
            self.random_state,
        )

        self.models = get_models(self.problem_type)

        results = []
        trained_models = {}

        for name, model in self.models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            metrics = compute_metrics(self.problem_type, y_test, y_pred)

            trained_models[name] = model
            results.append({"Model": name, **metrics})

        self.results = pd.DataFrame(results)

        if self.problem_type == "classification":
            self.results = self.results.sort_values(
                by="Accuracy",
                ascending=False,
            ).reset_index(drop=True)
        else:
            self.results = self.results.sort_values(
                by="R2 Score",
                ascending=False,
            ).reset_index(drop=True)

        if not self.results.empty:
            best_name = self.results.iloc[0]["Model"]
            self.best_model_name = best_name
            self.best_model = trained_models[best_name]

        self.trained_models = trained_models

        return self.results

    def predict(self, data):
        """
        Predict using the best trained model.
        """
        if self.best_model is None:
            raise ValueError("No trained model found. Run compare() first.")

        return self.best_model.predict(data)

    def save(self, path: str):
        """
        Save the best trained model.
        """
        save_model(self.best_model, path)