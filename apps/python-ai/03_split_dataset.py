import pandas as pd

from sklearn.model_selection import train_test_split

INPUT_FILE="../dataset/processed/reviews_features.csv"

TRAIN_FILE="../dataset/processed/train.csv"

VALIDATION_FILE="../dataset/processed/validation.csv"

TEST_FILE="../dataset/processed/test.csv"

df=pd.read_csv(INPUT_FILE)
print("Total dataset size:", len(df))

train_df,temp_df=train_test_split(df,test_size=0.30,stratify=df["label"],random_state=42)

validation_df,test_df=train_test_split(temp_df,test_size=0.50,stratify=temp_df["label"],random_state=42)

train_df.to_csv(TRAIN_FILE,index=False)
validation_df.to_csv(VALIDATION_FILE,index=False)
test_df.to_csv(TEST_FILE,index=False)

print("\nDataset sizes:")
print("Training:", len(train_df))
print("Validation:", len(validation_df))
print("Testing:", len(test_df))


print("\nTraining label distribution:")
print(train_df["label"].value_counts(normalize=True))


print("\nValidation label distribution:")
print(validation_df["label"].value_counts(normalize=True))


print("\nTesting label distribution:")
print(test_df["label"].value_counts(normalize=True))


print("\nFiles saved successfully.")