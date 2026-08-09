import pandas as pd
def analyze_sentences(text):
    sentence_count=0
    excalamtion_count=0
    prev=False

    for char in text:
        if char in ".!?":
            if not prev:
                sentence_count+=1
            if char=="!":
                excalamtion_count+=1
            prev=True    
        else:
            prev=False 
    return sentence_count,excalamtion_count    
df=pd.read_csv("../dataset/processed/reviews_clean.csv")
df["review_length"]=df["review"].str.len()
print(df[["review", "review_length"]].head())
print(df.columns.tolist())
df["word_count"]=df["review"].str.split().str.len()
print(df["word_count"].head())
df[["sentence_count", "exclamation_count"]] = (
    df["review"]
    .apply(analyze_sentences)
    .apply(pd.Series)
)
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