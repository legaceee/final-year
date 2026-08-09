import pandas as pd
import string
def analyze_sentences(text):
    sentence_count=0
    exclamtion_count=0
    prev=False

    for char in text:
        if char in ".!?":
            if not prev:
                sentence_count+=1
            if char=="!":
                exclamtion_count+=1
            prev=True    
        else:
            prev=False 
    if sentence_count==0:
        sentence_count=1
    return sentence_count,exclamtion_count   

def uppercase_ratio(text):
     uppercase_count=0
     character_count=0
     for char in text:
         if char.isupper():
             uppercase_count+=1
             character_count+=1
         elif char.isalpha():
              character_count+=1
     if character_count==0:
         return 0         
     return uppercase_count/character_count

def punctuation_ratio(text):
    punctuation_count=0
    word_count=0
    for char in text:
        if char in string.punctuation:
            punctuation_count+=1
            word_count+=1
        elif char.isalnum():
            word_count+=1   
    if word_count==0:
        return 0
    return punctuation_count/word_count       
df=pd.read_csv("../dataset/processed/reviews_clean.csv")
df["review_length"]=df["review"].str.len()

df["word_count"]=df["review"].str.split().str.len()

df[["sentence_count", "exclamation_count"]] = (
    df["review"]
    .apply(analyze_sentences)
    .apply(pd.Series)
)


df["uppercase_ratio"]=df["review"].apply(uppercase_ratio)
print(
    df.groupby("label")[
        [
            "review_length",
            "word_count",
            "sentence_count",
            "exclamation_count",
            "uppercase_ratio"
        ]
    ].mean()
)

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