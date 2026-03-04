import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
df = pd.read_csv("hours_pass_dataset.csv")

print("✅ Dataset loaded")
print(df.head())

df["result_encoded"] = df["result"].map({"Fail": 0, "Pass": 1})

print("\n✅ After Encoding Target:")
print(df[["result", "result_encoded"]].head())
# -----------------------------
# 3️⃣ Select X and y
# -----------------------------
X = df[["hours_studied"]]    # feature
y = df["result_encoded"]     # target (0/1)


# -----------------------------
# 4️⃣ Train–Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# -----------------------------
# 5️⃣ Create Model (NO pipeline)
# -----------------------------
model = LogisticRegression(max_iter=1000)


# -----------------------------
# 6️⃣ Train Model
# -----------------------------
model.fit(X_train, y_train)
print("\n✅ Model training completed")

# -----------------------------
# 7️⃣ Predict & Evaluate
# -----------------------------
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print("\n✅ Accuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, predictions))
joblib.dump(model, "hours_pass_model.pkl")
print("\n✅ Model saved as hours_pass_model.pkl")