import pandas as pd

df=pd.read_csv("../dataset/processed/reviews_clean.csv")
df["review_length"]=df["review"].str.len()
print(df[["review", "review_length"]].head())
print(df.columns.tolist())
df["word_count"]=df["review"].str.split().str.len()
print(df["word_count"].head())
