import pandas as pd

INPUT_FILE = "../dataset/raw/final_labeled_fake_reviews.csv"
OUTPUT_FILE = "../dataset/processed/reviews_clean.csv"
# read the file
df = pd.read_csv(INPUT_FILE)
df = df[
    [
        "rating",
        "title",
        "text",
        "helpful_vote",
        "verified_purchase",
        "label",
    ]
]
df = df.dropna(subset=["title", "text"])

df["title"] = df["title"].astype(str).str.strip()
df["text"] = df["text"].astype(str).str.strip()

# Remove empty title/text
df = df[
    (df["title"] != "") &
    (df["text"] != "")
]
df["review"] = (
    "[TITLE] "
    + df["title"]
    + " [BODY] "
    + df["text"]
)
df = df.drop_duplicates(subset=["review"])
df = df[
    df["review"].str.split().str.len() >= 5
]
df = df.reset_index(drop=True)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("=" * 40)
print("Dataset Cleaning Complete")
print("=" * 40)

print(f"Total Reviews : {len(df)}")

print("\nLabel Distribution")

print(df["label"].value_counts())



print("\nSaved to:")

print(OUTPUT_FILE)