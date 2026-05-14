import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv("dataset/train.csv")

# Combine title and text columns
df['content'] = df['title'].astype(str) + " " + df['text'].astype(str)

# Features and labels
X = df['content']
y = df['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(
    stop_words='english',
    max_df=0.7
)

# Transform text data
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Logistic Regression model
model = LogisticRegression()

# Train model
model.fit(X_train_tfidf, y_train)

# Predictions
y_pred = model.predict(X_test_tfidf)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Training Complete!")
print("Accuracy:", accuracy)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

# Save vectorizer
pickle.dump(tfidf, open("vectorizer.pkl", "wb"))

print("Model and Vectorizer saved successfully!")