# import pandas as pd

# df=pd.read_csv("../dataset/raw/final_labeled_fake_reviews.csv")

# print(df.head())
# print("\nshape")
# print(df.shape)
# print("\nColumns")
# print(df.columns)
# print("\nMissing values")
# print(df.isnull().sum())

# print("\nData types")
# print(df.dtypes)
# print("\nLabel Distribution")
# print(df["label"].value_counts(normalize=True) * 100)
import pandas as pd
df=pd.read_csv("../dataset/raw/final_labeled_fake_reviews.csv")
df=df[["rating","title","text","helpful_vote","verified_purchase","label"]]
print(df)
df=df.dropna(subset=["title","text"])
df["review"]= "[TITLE]" + " "+df["title"]+" "+"[BODY]"+" "+df["text"]
print(df["review"])
df=df.drop_duplicates(subset=["review"])
df=df[df["review"].str.split().str.len()>5]
print("Rows after preprocessing:", len(df))

print("\nLabel distribution:")
print(df["label"].value_counts())