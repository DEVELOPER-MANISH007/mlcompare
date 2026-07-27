<div align="center">

# 🚀 MLCompare

### Compare Machine Learning Models in Just a Few Lines of Code

A lightweight Python package to compare multiple Machine Learning models for **Classification** and **Regression**, evaluate performance, and save the best model effortlessly.

[![PyPI version](https://img.shields.io/pypi/v/mlcompare-dev.svg)](https://pypi.org/project/mlcompare-dev/)
[![Python Version](https://img.shields.io/pypi/pyversions/mlcompare-dev.svg)](https://pypi.org/project/mlcompare-dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/mlcompare-dev)](https://pypi.org/project/mlcompare-dev/)
[![GitHub stars](https://img.shields.io/github/stars/Developer-Manish007/mlcompare?style=social)](https://github.com/Developer-Manish007/mlcompare)

</div>

---

# 📦 Installation

```bash
pip install mlcompare-dev
```

---

# ✨ Features

- ✅ Automatic Classification & Regression support
- ✅ Compare multiple Machine Learning models
- ✅ Performance metrics comparison
- ✅ Save trained models
- ✅ Load saved models
- ✅ Clean and beginner-friendly API
- ✅ Built with Scikit-Learn

---

# 🚀 Quick Start

```python
from mlcompare import MLCompare
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load Dataset
X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create MLCompare Object
mc = MLCompare()

# Train Models
mc.fit(X_train, y_train)

# Compare Models
results = mc.compare()

print(results)
```

---

# 💾 Save Model

```python
mc.save("best_model.pkl")
```

---

# 📂 Load Model

```python
from mlcompare import load_model

model = load_model("best_model.pkl")
```

---

# 📊 Supported Models

## Classification

- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Support Vector Machine
- Gaussian Naive Bayes

## Regression

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- KNeighbors Regressor
- Support Vector Regressor

---

# 📈 Project Structure

```
mlcompare/
│
├── mlcompare/
│   ├── core.py
│   ├── models.py
│   ├── metrics.py
│   ├── save.py
│   ├── utils.py
│   ├── version.py
│   └── __init__.py
│
├── examples/
├── README.md
├── setup.py
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# 🛣️ Roadmap

## v0.2.0

- [ ] StandardScaler
- [ ] MinMaxScaler
- [ ] RobustScaler
- [ ] Cross Validation
- [ ] More Evaluation Metrics

## v0.3.0

- [ ] Hyperparameter Tuning
- [ ] Feature Importance
- [ ] Model Explainability

## v1.0.0

- [ ] AutoML Workflow
- [ ] Pipeline Support
- [ ] SHAP Integration
- [ ] XGBoost
- [ ] LightGBM
- [ ] CatBoost

---

# 🤝 Contributing

Contributions, feature requests, and bug reports are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Manish Kumar**

- GitHub: https://github.com/Developer-Manish007
- PyPI: https://pypi.org/project/mlcompare-dev/

---

<div align="center">

### ⭐ If you like this project, don't forget to give it a Star ⭐

</div>
