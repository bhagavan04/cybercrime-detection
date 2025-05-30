from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from .utils import detect_scam_regex
import joblib

class ScamDetector:
    def __init__(self):
        self.messages = [
            "Your bank account will be blocked. Send OTP to verify.",
            "URGENT: Your SIM will be deactivated in 24 hours.",
            "Claim your lottery prize now!",
            "See you at lunch.",
            "Reminder: dentist appointment tomorrow."
        ]
        self.labels = [1, 1, 1, 0, 0]  # 1 = scam, 0 = safe
        self.vectorizer = CountVectorizer()
        self.classifier = LogisticRegression()
        self.train_model()

    def train_model(self):
        X = self.vectorizer.fit_transform(self.messages)
        self.classifier.fit(X, self.labels)

    def predict(self, message: str) -> dict:
        x = self.vectorizer.transform([message])
        ml_flag = bool(self.classifier.predict(x)[0])
        regex_flag = detect_scam_regex(message)
        is_scam = ml_flag or regex_flag
        return {
            "message": message,
            "ml_flag": ml_flag,
            "regex_flag": regex_flag,
            "scam": is_scam
        }

    def save(self, path="scam_detector.pkl"):
        joblib.dump((self.vectorizer, self.classifier), path)

    def load(self, path="scam_detector.pkl"):
        self.vectorizer, self.classifier = joblib.load(path)
