<div align="center">

# 🚀 MLCompare

### Compare Machine Learning Models in Just a Few Lines of Code

A lightweight, beginner-friendly Python package for **Classification** and **Regression** that helps you train, evaluate, compare, and save Machine Learning models with a simple API.

[![PyPI version](https://img.shields.io/pypi/v/mlcompare-dev.svg)](https://pypi.org/project/mlcompare-dev/)
[![Python Version](https://img.shields.io/pypi/pyversions/mlcompare-dev.svg)](https://pypi.org/project/mlcompare-dev/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/mlcompare-dev.svg)](https://pypi.org/project/mlcompare-dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Developer-Manish007/mlcompare?style=social)](https://github.com/Developer-Manish007/mlcompare)

[**📦 View on PyPI**](https://pypi.org/project/mlcompare-dev/) &nbsp; • &nbsp; [**💻 View on GitHub**](https://github.com/Developer-Manish007/mlcompare)

</div>

---

## 🧠 What is MLCompare?

Machine Learning experimentation often involves repeating the same workflow for multiple algorithms:

**Prepare Data → Select Model → Train → Evaluate → Compare**

Doing this manually for every model can lead to repetitive code and slower experimentation.

**MLCompare** is designed to simplify this process by providing a reusable interface for comparing multiple Machine Learning models for **Classification** and **Regression** tasks.

> **Goal:** Reduce repetitive ML boilerplate and make model comparison simple, fast, and beginner-friendly.

---

## ✨ Features

- 🎯 **Classification & Regression** support
- 🤖 **Multiple model comparison** in a single workflow
- 📊 **Performance evaluation** and result comparison
- 🏆 **Best model selection**
- 💾 **Save trained models**
- 📂 **Load saved models**
- 🔮 **Prediction support**
- 🧩 **Simple and beginner-friendly API**
- 🐍 Built with the **Scikit-Learn** ecosystem

---

## 📦 Installation

### Install from PyPI

```bash
pip install mlcompare-dev
```

### Install locally for development

```bash
git clone https://github.com/Developer-Manish007/mlcompare.git
cd mlcompare
pip install -e .
```

### 🔗 Important Links

| Resource | Link |
|---|---|
| 📦 PyPI Package | https://pypi.org/project/mlcompare-dev/ |
| 💻 GitHub Repository | https://github.com/Developer-Manish007/mlcompare |

---

## 🚀 Quick Start

```python
from mlcompare import MLCompare
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
X, y = load_iris(return_X_y=True)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create MLCompare object
mc = MLCompare()

# Train models
mc.fit(X_train, y_train)

# Compare models
results = mc.compare()

print(results)
```

---

## 💾 Save a Model

Save a trained model for later use:

```python
mc.save("best_model.pkl")
```

---

## 📂 Load a Model

```python
from mlcompare import load_model

model = load_model("best_model.pkl")
```

---

## 📊 Supported Models

### 🔵 Classification

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Gaussian Naive Bayes

### 🟢 Regression

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- K-Neighbors Regressor
- Support Vector Regressor

---

## 🔄 MLCompare Workflow

```text
              ┌─────────────────┐
              │     Dataset     │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │   Data Setup    │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │  Model Training │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │    Evaluation   │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Model Comparison│
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │   Best Model    │
              └─────────────────┘
```

The workflow is designed to make it easier to experiment with multiple models without rewriting the same comparison logic repeatedly.

---

## 🧪 Example Use Case

Suppose you have a classification dataset and want to test several algorithms.

Instead of creating separate training and evaluation code for every model, MLCompare provides a common workflow where the models can be trained and compared together.

This is especially useful for:

- 📚 Learning Machine Learning
- 🔬 Model experimentation
- 📊 Exploratory model comparison
- 🧑‍💻 Data Science projects
- ⚡ Rapid prototyping

---

## 📁 Project Structure

```text
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

## 🛣️ Roadmap

### v0.2.0

- [ ] StandardScaler
- [ ] MinMaxScaler
- [ ] RobustScaler
- [ ] Cross Validation
- [ ] More Evaluation Metrics

### v0.3.0

- [ ] Hyperparameter Tuning
- [ ] Feature Importance
- [ ] Model Explainability

### v1.0.0

- [ ] AutoML Workflow
- [ ] Pipeline Support
- [ ] SHAP Integration
- [ ] XGBoost
- [ ] LightGBM
- [ ] CatBoost

---

## 🤝 Contributing

Contributions, feature requests, improvements, and bug reports are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Open a Pull Request

---

## 📄 License

MLCompare is released under the **MIT License**.

---

## 👨‍💻 Author

### Manish Kumar

Aspiring Data Scientist & Machine Learning Engineer

- 💻 GitHub: https://github.com/Developer-Manish007
- 📦 PyPI: https://pypi.org/project/mlcompare-dev/

---

<div align="center">

## ⭐ Support MLCompare

If you find MLCompare useful, consider giving the repository a ⭐ on GitHub.

[**📦 Install from PyPI**](https://pypi.org/project/mlcompare-dev/) &nbsp; • &nbsp; [**⭐ Star on GitHub**](https://github.com/Developer-Manish007/mlcompare)

### Built with 🐍 Python & ❤️ for the Machine Learning community

</div>
