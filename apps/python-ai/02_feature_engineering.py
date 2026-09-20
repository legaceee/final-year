import pandas as pd
import string


def analyze_sentences(text):
    sentence_count = 0
    exclamation_count = 0
    question_count = 0

    previous_was_punctuation = False

    for char in text:
        if char in ".!?":

            if not previous_was_punctuation:
                sentence_count += 1

            if char == "!":
                exclamation_count += 1

            if char == "?":
                question_count += 1

            previous_was_punctuation = True

        else:
            previous_was_punctuation = False

    if sentence_count == 0:
        sentence_count = 1

    return (
        sentence_count,
        exclamation_count,
        question_count
    )


def uppercase_ratio(text):
    uppercase_count = 0
    alphabetic_count = 0

    for char in text:
        if char.isalpha():
            alphabetic_count += 1

            if char.isupper():
                uppercase_count += 1

    if alphabetic_count == 0:
        return 0

    return uppercase_count / alphabetic_count


def punctuation_ratio(text):
    punctuation_count = 0
    relevant_character_count = 0

    for char in text:

        if char in string.punctuation:
            punctuation_count += 1
            relevant_character_count += 1

        elif char.isalnum():
            relevant_character_count += 1

    if relevant_character_count == 0:
        return 0

    return punctuation_count / relevant_character_count


def average_word_length(text):
    words = text.split()

    if len(words) == 0:
        return 0

    total_characters = sum(len(word) for word in words)

    return total_characters / len(words)


def lexical_diversity(text):
    words = text.lower().split()

    if len(words) == 0:
        return 0

    unique_words = set(words)

    return len(unique_words) / len(words)


# Load processed dataset
df = pd.read_csv(
    "../dataset/processed/reviews_clean.csv"
)

# Confirm missing values
print("Missing title:", df["title"].isna().sum())
print("Missing text:", df["text"].isna().sum())

# Combine title and text for style analysis
df["style_text"] = (
    df["title"].fillna("").astype(str)
    + " "
    + df["text"].fillna("").astype(str)
)

# Basic text features
df["review_length"] = df["style_text"].str.len()

df["word_count"] = (
    df["style_text"].str.split().str.len()
)

# Sentence-based features
df[
    [
        "sentence_count",
        "exclamation_count",
        "question_count"
    ]
] = (
    df["style_text"]
    .apply(analyze_sentences)
    .apply(pd.Series)
)

# Character-based features
df["uppercase_ratio"] = (
    df["style_text"].apply(uppercase_ratio)
)

df["punctuation_ratio"] = (
    df["style_text"].apply(punctuation_ratio)
)

# Word-based features
df["average_word_length"] = (
    df["style_text"].apply(average_word_length)
)

df["lexical_diversity"] = (
    df["style_text"].apply(lexical_diversity)
)

# Feature summary
feature_columns = [
    "review_length",
    "word_count",
    "sentence_count",
    "exclamation_count",
    "question_count",
    "uppercase_ratio",
    "punctuation_ratio",
    "average_word_length",
    "lexical_diversity"
]

print("\nFeature Summary:")
print(df[feature_columns].describe())

print("\nFeature Means by Label:")
print(
    df.groupby("label")[feature_columns].mean()
)

# Preview
print("\nFeature Preview:")
print(
    df[
        feature_columns + ["label"]
    ].head(10)
)