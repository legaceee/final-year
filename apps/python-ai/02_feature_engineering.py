import pandas as pd

df=pd.read_csv("../dataset/raw/final_labeled_fake_reviews.csv")

print(df[df["label"]==1])
