import pandas as pd


TRAIN_FILE = "../dataset/processed/train.csv"
VALIDATION_FILE = "../dataset/processed/validation.csv"
TEST_FILE = "../dataset/processed/test.csv"


train_df = pd.read_csv(TRAIN_FILE)
validation_df = pd.read_csv(VALIDATION_FILE)
test_df = pd.read_csv(TEST_FILE)


# --------------------------------
# 1. Check duplicate reviews
# --------------------------------

train_reviews = set(train_df["review"])
validation_reviews = set(validation_df["review"])
test_reviews = set(test_df["review"])


print("Duplicate review checks:")

print(
    "Train ∩ Validation:",
    len(train_reviews.intersection(validation_reviews))
)

print(
    "Train ∩ Test:",
    len(train_reviews.intersection(test_reviews))
)

print(
    "Validation ∩ Test:",
    len(validation_reviews.intersection(test_reviews))
)


# --------------------------------
# 2. Check user overlap
# --------------------------------

train_users = set(train_df["user_id"])
validation_users = set(validation_df["user_id"])
test_users = set(test_df["user_id"])


print("\nUser overlap checks:")

print(
    "Train ∩ Validation:",
    len(train_users.intersection(validation_users))
)

print(
    "Train ∩ Test:",
    len(train_users.intersection(test_users))
)

print(
    "Validation ∩ Test:",
    len(validation_users.intersection(test_users))
)