import re

scam_keywords = [
    r'\bOTP\b', r'\bbank\b', r'\burgent\b', r'\bsim\b',
    r'blocked', r'\baccount\b', r'\bverify\b', r'\bclick here\b', r'lottery'
]

def detect_scam_regex(message: str) -> bool:
    for pattern in scam_keywords:
        if re.search(pattern, message, re.IGNORECASE):
            return True
    return False
