import os
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer


# -----------------------------
# 1. File paths
# -----------------------------

TRAIN_FILE = "../dataset/processed/train.csv"
VALIDATION_FILE = "../dataset/processed/validation.csv"
TEST_FILE = "../dataset/processed/test.csv"

OUTPUT_DIR = "../dataset/embeddings"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# -----------------------------
# 2. Load the datasets
# -----------------------------

train_df = pd.read_csv(TRAIN_FILE)
validation_df = pd.read_csv(VALIDATION_FILE)
test_df = pd.read_csv(TEST_FILE)

print("Datasets loaded")

print("Training reviews:", len(train_df))
print("Validation reviews:", len(validation_df))
print("Test reviews:", len(test_df))


# -----------------------------
# 3. Load the MiniLM model
# -----------------------------

print("\nLoading MiniLM model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("MiniLM model loaded")


# -----------------------------
# 4. Generate embeddings
# -----------------------------

def generate_embeddings(df, dataset_name):
    print(f"\nGenerating embeddings for {dataset_name}...")

    reviews = df["review"].fillna("").tolist()

    embeddings = model.encode(
        reviews,
        batch_size=32,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    embeddings = np.asarray(embeddings, dtype=np.float32)

    output_path = os.path.join(
        OUTPUT_DIR,
        f"{dataset_name}_embeddings.npy"
    )

    np.save(output_path, embeddings)

    print(f"{dataset_name} embeddings saved")
    print("Shape:", embeddings.shape)
    print("Saved at:", output_path)

    return embeddings


# -----------------------------
# 5. Generate each dataset
# -----------------------------

train_embeddings = generate_embeddings(
    train_df,
    "train"
)

validation_embeddings = generate_embeddings(
    validation_df,
    "validation"
)

test_embeddings = generate_embeddings(
    test_df,
    "test"
)


# -----------------------------
# 6. Save labels separately
# -----------------------------

np.save(
    os.path.join(OUTPUT_DIR, "train_labels.npy"),
    train_df["label"].to_numpy()
)

np.save(
    os.path.join(OUTPUT_DIR, "validation_labels.npy"),
    validation_df["label"].to_numpy()
)

np.save(
    os.path.join(OUTPUT_DIR, "test_labels.npy"),
    test_df["label"].to_numpy()
)


# -----------------------------
# 7. Final summary
# -----------------------------

print("\nEmbedding generation completed")

print("Train shape:", train_embeddings.shape)
print("Validation shape:", validation_embeddings.shape)
print("Test shape:", test_embeddings.shape)