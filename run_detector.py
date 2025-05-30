from scam_message_detector import ScamDetector

detector = ScamDetector()

messages = [
    "Your account will be blocked. Send OTP now.",
    "Click here to win an iPhone!",
    "Dinner at my place?",
    "Your SIM will be disabled. Urgent action needed!"
]

for msg in messages:
    result = detector.predict(msg)
    print(f"\nMessage: {result['message']}")
    print(f"ML Flag: {result['ml_flag']} | Regex Flag: {result['regex_flag']}")
    print("🔴 SCAM DETECTED" if result['scam'] else "✅ Safe message")
