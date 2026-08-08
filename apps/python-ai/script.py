import pandas as pd
df=pd.read_csv("../dataset/raw/final_labeled_fake_reviews.csv")
# print("user review burst:")
# print(df["user_review_burst"].describe())

# print("\n99999 count:")
# print((df["user_review_burst"] == 99999).sum())

# print("\nOther values:")
# print(df.loc[df["user_review_burst"]!=99999,["user_id","timestamp","user_timestamp","user_review_burst","label"]].head(20))

print(df.groupby("label")["user_review_burst"].agg(["count","mean","median","min","max"]))

print("\n99999 by label:")
print(pd.crosstab(df["label"],df["user_review_burst"]==99999,normalize="index"))