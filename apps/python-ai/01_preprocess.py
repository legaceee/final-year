import pandas as pd

INPUT_FILE = "../dataset/raw/final_labeled_fake_reviews.csv"
OUTPUT_FILE = "../dataset/processed/reviews_clean.csv"
# read the file
df = pd.read_csv(INPUT_FILE)
# df = df[
#     [
#         "rating",
#         "title",
#         "text",
#         "helpful_vote",
#         "verified_purchase",
#         "label",
#     ]
# ]
selected_columns = [
    "rating",
    "title",
    "text",
    "helpful_vote",
    "verified_purchase",
    "user_id",
    "timestamp",
    "user_timestamp",
    "user_review_burst",
    "label"
]

df = df[selected_columns].copy()
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
print(df[[
    "user_id",
    "timestamp",
    "user_timestamp",
    "user_review_burst",
    "label"
]].head(10))

print("\nData types:")
print(df[[
    "user_id",
    "timestamp",
    "user_timestamp",
    "user_review_burst"
]].dtypes)
print("\nBurst statistics:")
print(df["user_review_burst"].describe(percentiles=[
    0.50,
    0.90,
    0.95,
    0.99
]))

print("\nSmallest burst values:")
print(
    df["user_review_burst"]
    .sort_values()
    .head(20)
    .to_list()
)

print("\nLargest burst values:")
print(
    df["user_review_burst"]
    .sort_values(ascending=False)
    .head(20)
    .to_list()
)

print("\nUser timestamp statistics:")
print(df["user_timestamp"].describe())

print("\nUser timestamp examples:")
print(df["user_timestamp"].head(20).to_list())

print("\nBurst and timestamp sample:")
print(
    df[
        [
            "user_timestamp",
            "user_review_burst",
            "label"
        ]
    ].head(20).to_string(index=False)
)
print("\nBurst statistics by label:")

print(
    df.groupby("label")["user_review_burst"]
      .agg([
          "count",
          "mean",
          "median",
          "min",
          "max"
      ])
)
default_burst = 99999.0

print("\nDefault burst value by label:")

print(
    pd.crosstab(
        df["label"],
        df["user_review_burst"] == default_burst,
        normalize="index"
    )
)