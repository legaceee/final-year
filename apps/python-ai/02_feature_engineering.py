import pandas as pd
def count_Sentences(review):
     count = review.count(".") + review.count("!") + review.count("?")
     if count == 0:
        return 1
     return count
def count_exclamation(review):
     count=review.count("!")
     return count
df=pd.read_csv("../dataset/processed/reviews_clean.csv")
df["review_length"]=df["review"].str.len()
print(df[["review", "review_length"]].head())
print(df.columns.tolist())
df["word_count"]=df["review"].str.split().str.len()
print(df["word_count"].head())
df["sentence_count"]=df["review"].apply(count_Sentences)
df["excalamation count"]=df["review"].str.count("!")
print(df["exclamation count"])

# review_length
# word_count
# sentence_count
# to do 
# average_word_length
# exclamation_count
# question_count
# uppercase_ratio
# punctuation_ratio
# lexical_diversity