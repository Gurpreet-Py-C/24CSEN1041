import re
def check_password_strength(password: str):
    score = 0
    feedback = []
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Make your password at least 8–12 characters long.")
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A–Z).")
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a–z).")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number (0–9).")
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$...).")
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeating the same character multiple times.")
    else:
        score += 1
    common_patterns = ["123", "password", "qwerty", "abc"]
    if any(pat in password.lower() for pat in common_patterns):
        feedback.append("Avoid common patterns like '123', 'password', or 'qwerty'.")
    else:
        score += 1
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 6:
        strength = "Moderate"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"
    return strength, score, feedback
password = input("Enter your password: ")
strength, score, suggestions = check_password_strength(password)
print("\nPassword Strength:", strength)
print("Score:", score, "/10")
if suggestions:
    print("\nSuggestions to improve your password:")
    for i, tip in enumerate(suggestions, 1):
        print(f"{i}. {tip}")
else:
    print("\nExcellent! Your password is strong and secure")