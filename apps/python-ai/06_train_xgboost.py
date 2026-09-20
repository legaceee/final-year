import os
import time

import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# ---------------------------------
# 1. File paths
# ---------------------------------

EMBEDDINGS_DIR = "../dataset/embeddings"

TRAIN_FILE = "../dataset/processed/train.csv"
VALIDATION_FILE = "../dataset/processed/validation.csv"
TEST_FILE = "../dataset/processed/test.csv"


# ---------------------------------
# 2. Load embeddings
# ---------------------------------

print("Loading embeddings...")

X_train = np.load(
    os.path.join(EMBEDDINGS_DIR, "train_embeddings.npy")
)

X_validation = np.load(
    os.path.join(EMBEDDINGS_DIR, "validation_embeddings.npy")
)

X_test = np.load(
    os.path.join(EMBEDDINGS_DIR, "test_embeddings.npy")
)


# ---------------------------------
# 3. Load labels
# ---------------------------------

train_df = pd.read_csv(TRAIN_FILE)
validation_df = pd.read_csv(VALIDATION_FILE)
test_df = pd.read_csv(TEST_FILE)

y_train = train_df["label"].to_numpy()
y_validation = validation_df["label"].to_numpy()
y_test = test_df["label"].to_numpy()


# ---------------------------------
# 4. Verify the data
# ---------------------------------

print("\nData verification")

print("X_train shape:", X_train.shape)
print("X_validation shape:", X_validation.shape)
print("X_test shape:", X_test.shape)

print("y_train shape:", y_train.shape)
print("y_validation shape:", y_validation.shape)
print("y_test shape:", y_test.shape)

assert len(X_train) == len(y_train)
assert len(X_validation) == len(y_validation)
assert len(X_test) == len(y_test)

print("Data verification passed")


# ---------------------------------
# 5. Create the XGBoost model
# ---------------------------------

print("\nCreating XGBoost model...")

model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="binary:logistic",
    eval_metric="logloss",
    tree_method="hist",
    random_state=42,
    n_jobs=-1
)


# ---------------------------------
# 6. Train the model
# ---------------------------------

print("Training started...")

start_time = time.perf_counter()

model.fit(
    X_train,
    y_train,
    eval_set=[(X_validation, y_validation)],
    verbose=False
)

training_time = time.perf_counter() - start_time

print(f"Training completed in {training_time:.2f} seconds")


# ---------------------------------
# 7. Generate predictions
# ---------------------------------

print("\nGenerating test predictions...")

start_time = time.perf_counter()

y_probability = model.predict_proba(X_test)[:, 1]

y_prediction = (y_probability >= 0.5).astype(int)

prediction_time = time.perf_counter() - start_time


# ---------------------------------
# 8. Evaluate the model
# ---------------------------------

accuracy = accuracy_score(y_test, y_prediction)

precision = precision_score(
    y_test,
    y_prediction,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_prediction,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_prediction,
    zero_division=0
)


print("\nModel evaluation")

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")

print("\nClassification report")

print(
    classification_report(
        y_test,
        y_prediction,
        zero_division=0
    )
)

print("Confusion matrix")

print(
    confusion_matrix(
        y_test,
        y_prediction
    )
)

print(f"\nPrediction time: {prediction_time:.6f} seconds")
print(f"Prediction time per review: {prediction_time / len(X_test):.8f} seconds")


# ---------------------------------
# 9. Save the trained model
# ---------------------------------

MODEL_DIR = "../models"

os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "xgboost_minilm_baseline.json"
)

model.save_model(MODEL_PATH)

print("\nModel saved at:")
print(MODEL_PATH)