import streamlit as st
import re
import random
import string

def check_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special char check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    score, feedback = check_strength(password)
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider improving it.")
    else:
        st.error("❌ Weak Password - Please fix the issues below:")
        for f in feedback:
            st.write(f)

if st.button("Suggest a Strong Password"):
    strong_pwd = generate_password()
    st.info(f"Suggested strong password: `{strong_pwd}`")
