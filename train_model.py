import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)

print("Loading prepared dataset...")

df = pd.read_csv("data_sample.csv")

print("Dataset shape:", df.shape)

# Select input features
features = [
    "step",
    "type",
    "amount",
    "oldbalanceOrg",
    "newbalanceOrig",
    "oldbalanceDest",
    "newbalanceDest"
]

X = df[features]
y = df["isFraud"]

# Separate numerical and categorical columns
numeric_features = [
    "step",
    "amount",
    "oldbalanceOrg",
    "newbalanceOrig",
    "oldbalanceDest",
    "newbalanceDest"
]

categorical_features = ["type"]

# Convert transaction type into numerical form
preprocessor = ColumnTransformer(
    transformers=[
        ("category",
         OneHotEncoder(handle_unknown="ignore"),
         categorical_features),
        ("numbers", "passthrough", numeric_features)
    ]
)

# Create Random Forest model
classifier = RandomForestClassifier(
    n_estimators=50,
    class_weight="balanced_subsample",
    random_state=42,
    n_jobs=-1
)

model = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", classifier)
])

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# Train model
print("\nTraining Random Forest model...")

model.fit(X_train, y_train)

print("\nModel training completed!")

# Evaluate model
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nROC-AUC Score:")
print(roc_auc_score(y_test, probabilities))

# Save trained model
os.makedirs("Model", exist_ok=True)

joblib.dump(model, "Model/fraud_model.pkl")

print("\nModel saved successfully!")
print("Location: Model/fraud_model.pkl")