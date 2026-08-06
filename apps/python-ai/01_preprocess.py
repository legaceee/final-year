import pandas as pd

INPUT_FILE = "../dataset/raw/final_labeled_fake_reviews.csv"
OUTPUT_FILE = "../dataset/processed/reviews_clean.csv"

df = pd.read_csv(INPUT_FILE)