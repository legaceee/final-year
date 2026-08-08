import pandas as pd
df=pd.read_csv("../dataset/raw/final_labeled_fake_reviews.csv")
# print("user review burst:")
# print(df["user_review_burst"].describe())

# print("\n99999 count:")
# print((df["user_review_burst"] == 99999).sum())

# print("\nOther values:")
# print(df.loc[df["user_review_burst"]!=99999,["user_id","timestamp","user_timestamp","user_review_burst","label"]].head(20))

# print(df.groupby("label")["user_review_burst"].agg(["count","mean","median","min","max"]))

# print("\n99999 by label:")
# print(pd.crosstab(df["label"],df["user_review_burst"]==99999,normalize="index"))

# other = df[df["user_review_burst"] != 99999]

# print(
#     other[
#         [
#             "user_id",
#             "timestamp",
#             "user_timestamp",
#             "user_review_burst",
#             "label"
#         ]
#     ].head(20).to_string(index=False)
# )
# print("\nUnique users among non-99999:")
# print(other["user_id"].nunique())

# print("\nRows per user:")
# print(other["user_id"].value_counts().head(20))

user_counts=df["user_id"].value_counts()
df["user_review_count"]=df["user_id"].map(user_counts)

print(df[["user_id","user_review_count","label"]].head(20))

print(df.groupby("label")["user_review_count"].agg(["mean","median","max"]))
