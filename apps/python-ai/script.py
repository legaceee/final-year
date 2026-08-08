import pandas as pd
df=pd.read_csv("../dataset/raw/final_labeled_fake_reviews.csv")
print("user review burst:")
print(df["user_review_burst"].describe())