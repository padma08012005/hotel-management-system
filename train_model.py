import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading dataset...")

# Load dataset
data = pd.read_csv("dataset/hotel_reviews.csv")

print("Dataset loaded successfully!")
print("Columns found:", data.columns)

# Ensure required columns exist
required_columns = ["city", "features", "review"]

for col in required_columns:
    if col not in data.columns:
        raise ValueError(f"Column '{col}' not found in dataset!")

# Fill missing values
data["city"] = data["city"].fillna("").astype(str)
data["features"] = data["features"].fillna("").astype(str)
data["review"] = data["review"].fillna("").astype(str)

# Combine important text columns (FIXED VERSION)
data["combined_features"] = data[["city", "features", "review"]].agg(" ".join, axis=1)

print("Creating TF-IDF matrix...")

# Convert text to numeric vectors
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(data["combined_features"])

print("Calculating similarity matrix...")

# Compute cosine similarity
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create model folder if not exists
if not os.path.exists("model"):
    os.makedirs("model")

# Save files properly using with open (clean method)
with open("model/data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("model/similarity.pkl", "wb") as f:
    pickle.dump(similarity, f)

with open("model/tfidf.pkl", "wb") as f:
    pickle.dump(tfidf, f)

print("Model trained and saved successfully!")