import joblib

# Load the saved pipeline
pipeline = joblib.load('resume_classifier.pkl')

def predict_resume_category(resume_text):
    prediction = pipeline.predict([resume_text])[0]  # Get predicted category
    probabilities = pipeline.predict_proba([resume_text])[0]  # Probabilities for all classes
    confidence = max(probabilities)  # Confidence score for predicted class
    return prediction, confidence

if __name__ == "__main__":
    sample_resume = input("Paste resume text here:\n")
    category, confidence = predict_resume_category(sample_resume)
    print(f"Predicted Category: {category}")
    print(f"Confidence Score: {confidence:.2f}")