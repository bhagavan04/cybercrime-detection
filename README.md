# cybercrime-detection
Cybercriminals exploit Telegram, WhatsApp, SMS, and social media for scams, fraud, fake docs, and harassment. Law enforcement lacks a smart, real-time system to detect and counter these threats.

# 🛡️ AI-Powered Scam Message Detector

A lightweight and extensible module for detecting scam messages (e.g., fake OTP requests, phishing, fraud alerts) using AI techniques. Designed for integration into larger cybercrime monitoring systems or as a standalone SMS/Telegram/WhatsApp bot service.


## 🔍 Problem Statement

Cybercriminals increasingly use digital messaging platforms (SMS, Telegram, WhatsApp) to send scam messages that:
- Trick users into sharing OTPs or banking details.
- Deliver phishing links via urgent or threatening language.
- Impersonate legitimate entities like banks, government bodies, etc.

Manual monitoring is **impractical at scale**, and users are often unable to identify scams. A scalable, intelligent, and automated detection system is needed to **analyze messages in real time** and raise alerts.

---

## 🧠 AI-Powered Approach

We use a **hybrid model** that combines:
- **Regex and keyword pattern matching** for rule-based detection.
- **Machine Learning (ML)** models trained on phishing/spam datasets for intelligent classification.
- Designed to be modular and scalable across languages and platforms.

---

## ✅ Solution Features

| Feature                          | Description |
|----------------------------------|-------------|
| 🔍 **Regex Matching**            | Identifies high-risk phrases (e.g., “Send OTP”, “Account blocked”). |
| 🧠 **ML Classifier**             | Logistic Regression model trained on scam/non-scam messages. |
| 📦 **Modular Python Package**    | Can be embedded into SMS bots, Telegram bots, or REST APIs. |
| 🌐 **Language-Agnostic**         | Extendable to support multilingual messages. |
| 🚨 **Real-time Alerts**          | Flags suspicious messages instantly. |

---

## 🔧 Tools & Technologies

| Purpose          | Tool / Library        |
|------------------|------------------------|
| NLP Preprocessing| NLTK, Regex            |
| Machine Learning | scikit-learn (Logistic Regression) |
| Data Vectorization | CountVectorizer       |
| OCR/Image Support (optional) | Tesseract OCR |
| Deployment Ready | Docker, Flask (API-ready) |

---

## 🚀 How It Works

1. **Message Input**: User inputs or the bot receives a text message.
2. **Regex Matching**: Checks for high-risk patterns (e.g., "send OTP", "click here").
3. **ML Classification**: Trained model classifies the message as scam or not.
4. **Alert**: If flagged, logs or alerts the appropriate system.

---

## 🧪 Example Usage

```bash
$ python scam_message_detector.py
