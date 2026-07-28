# 🚀 MLCompare

**MLCompare** is a beginner-friendly Python library to compare multiple Machine Learning models with just a few lines of code.

Instead of writing repetitive code for training and evaluating models, MLCompare automatically trains multiple algorithms, compares their performance, selects the best model, and allows prediction and model saving.

---

# ✨ Features

- ✅ Automatic Classification & Regression Detection
- ✅ Train Multiple ML Models
- ✅ Compare Model Performance
- ✅ Automatically Select Best Model
- ✅ Predict Using Best Model
- ✅ Save & Load Trained Model
- ✅ Simple Beginner-Friendly API

---

# 📦 Installation

```bash
pip install mlcompare
```

Or install locally

```bash
pip install -e .
```

---

# 📚 Supported Models

## Classification

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- Extra Trees

## Regression

- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- Extra Trees Regressor

---

# 🚀 Quick Start

```python
from mlcompare import MLCompare
import pandas as pd

df = pd.read_csv("data.csv")

ml = MLCompare(
    data=df,
    target="target"
)

results = ml.compare()

print(results)
```

---

# 🏆 Best Model

```python
print(ml.best_model_name)
```

---

# 🔮 Prediction

```python
new_data = df.drop(columns=["target"]).head()

predictions = ml.predict(new_data)

print(predictions)
```

---

# 💾 Save Model

```python
ml.save("best_model.pkl")
```

---

# 📂 Load Model

```python
ml.load("best_model.pkl")
```

---

# 📊 Example Output

| Model | Accuracy |
|--------|----------|
| SVM | 0.95 |
| Random Forest | 0.94 |
| Extra Trees | 0.93 |
| Logistic Regression | 0.91 |

---

# 📁 Project Structure

```
mlcompare/
│
├── core.py
├── models.py
├── metrics.py
├── utils.py
├── save.py
├── version.py
└── __init__.py
```

---

# 🛠 Requirements

- Python 3.10+
- pandas
- numpy
- scikit-learn
- joblib

---

# 📌 Roadmap

Upcoming Features

- Hyperparameter Tuning
- Cross Validation
- Feature Importance
- Confusion Matrix
- ROC-AUC Score
- StandardScaler Support
- Missing Value Handling
- Categorical Encoding
- XGBoost
- LightGBM
- CatBoost

---

# 🤝 Contributing

Contributions are welcome!

Feel free to open an Issue or submit a Pull Request.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

**Manish Kumar**

GitHub:
https://github.com/Developer-Manish007