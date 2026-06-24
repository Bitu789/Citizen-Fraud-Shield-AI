def detect_scam(text):

    text = text.lower()

    score = 0
    reasons = []

    scam_patterns = {
        # Banking
        "bank": ("Banking-related message", "Banking Scam"),
        "kyc": ("KYC verification request", "Banking Scam"),
        "account blocked": ("Account blocked threat", "Banking Scam"),
        "verify": ("Verification request", "Banking Scam"),

        # OTP
        "otp": ("OTP request detected", "OTP Scam"),

        # Lottery
        "lottery": ("Lottery fraud indicator", "Lottery Scam"),
        "reward": ("Reward scam indicator", "Lottery Scam"),
        "winner": ("Prize winning message", "Lottery Scam"),

        # Investment
        "investment": ("Investment scheme detected", "Investment Scam"),
        "double your money": ("Unrealistic return promise", "Investment Scam"),
        "profit guaranteed": ("Guaranteed profit claim", "Investment Scam"),

        # Digital Arrest
        "cbi": ("Fake law enforcement reference", "Digital Arrest Scam"),
        "customs": ("Fake customs investigation", "Digital Arrest Scam"),
        "ed": ("Enforcement Directorate reference", "Digital Arrest Scam"),
        "arrest": ("Arrest threat detected", "Digital Arrest Scam"),
        "video call": ("Forced video call pattern", "Digital Arrest Scam"),

        # Job Scam
        "job offer": ("Suspicious job offer", "Job Scam"),
        "registration fee": ("Advance payment request", "Job Scam"),
        "work from home": ("Work from home scam pattern", "Job Scam"),

        # UPI Scam
        "upi": ("UPI-related message", "UPI Scam"),
        "collect request": ("UPI collect request detected", "UPI Scam"),
        "refund": ("Fake refund pattern", "UPI Scam"),
        "payment link": ("Suspicious payment link", "UPI Scam"),

        # General
        "urgent": ("Urgency pressure tactic", "Fraud"),
        "click": ("Suspicious link request", "Fraud"),
        "immediately": ("Pressure tactic", "Fraud")
    }

    detected_types = []

    for keyword, (reason, scam_type) in scam_patterns.items():
        if keyword in text:
            score += 15
            reasons.append(reason)

            if scam_type not in detected_types:
                detected_types.append(scam_type)

    score = min(score, 100)

    if score >= 70:
        risk_level = "High"
    elif score >= 40:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    fraud_type = detected_types[0] if detected_types else "Safe"

    warning = ""

    if score >= 70:
        warning = """
⚠ HIGH RISK FRAUD DETECTED

Do NOT:
• Share OTP
• Transfer Money
• Click Links
• Continue Suspicious Calls
"""

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "fraud_type": fraud_type,
        "reasons": reasons,
        "warning": warning
    }