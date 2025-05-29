import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv('Resume.csv')

X = df['Resume_str']
y = df['Category']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Build pipeline: vectorizer + logistic regression
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('clf', LogisticRegression(max_iter=200))
])

# Train
pipeline.fit(X_train, y_train)

# Predict & evaluate
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

import joblib

# Save the trained pipeline to a file
joblib.dump(pipeline, 'resume_classifier.pkl')

print("Model pipeline saved as 'resume_classifier.pkl'")