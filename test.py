from mlcompare import MLCompare
import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    "age": np.random.randint(18, 60, 100),
    "salary": np.random.randint(20000, 100000, 100),
    "experience": np.random.randint(1, 20, 100),
    "target": np.random.randint(0, 2, 100),
})

ml = MLCompare(df, "target")

results = ml.compare()

print(results)

print("\nBest Model:")
print(ml.best_model_name)

new_data = df.drop(columns=["target"]).head()

pred = ml.predict(new_data)

print("\nPrediction:")
print(pred)

ml.save("best_model.pkl")

print("\nModel Saved Successfully!")