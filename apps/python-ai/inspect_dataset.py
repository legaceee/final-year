import pandas as pd

df=pd.read_csv("../dataset/raw/final_labeled_fake_reviews.csv")

print(df.head())
print("\nshape")
print(df.shape)
print("\nColumns")
print(df.columns)
print("\nMissing values")
print(df.isnull().sum())

print("\nData types")
print(df.dtypes)
print("\nLabel Distribution")
print(df.iloc[:, -1].value_counts())