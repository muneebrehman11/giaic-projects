import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate key once per app instance (in production, store securely)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# In-memory data storage: store data with unique IDs (simulate usernames or keys)
# Structure: { "data_id": {"encrypted_text": "...", "passkey": "hashed_passkey"} }
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

# Track failed attempts per session
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

# Simple login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)

    # Search for matching encrypted_text and passkey
    for data_id, data_entry in st.session_state.stored_data.items():
        if data_entry["encrypted_text"] == encrypted_text and data_entry["passkey"] == hashed_passkey:
            # Reset attempts on success
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()

    # Increment failed attempts
    st.session_state.failed_attempts += 1
    return None

st.title("🔒 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")
    st.write("Navigate using the sidebar.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    data_id = st.text_input("Enter a unique ID for your data (e.g., username or label):")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if data_id and user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            # Store by data_id
            st.session_state.stored_data[data_id] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            st.success(f"✅ Data stored securely under ID: {data_id}")
        else:
            st.error("⚠️ All fields are required!")

elif choice == "Retrieve Data":
    if st.session_state.failed_attempts >= 3 and not st.session_state.logged_in:
        st.warning("🔒 Too many failed attempts! Please reauthorize by logging in.")
        st.experimental_rerun()

    st.subheader("🔍 Retrieve Your Data")
    data_id = st.text_input("Enter your Data ID:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if data_id and passkey:
            if data_id in st.session_state.stored_data:
                encrypted_text = st.session_state.stored_data[data_id]["encrypted_text"]
                decrypted_text = decrypt_data(encrypted_text, passkey)
                if decrypted_text:
                    st.success(f"✅ Decrypted Data: {decrypted_text}")
                else:
                    attempts_left = 3 - st.session_state.failed_attempts
                    st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")
                    if st.session_state.failed_attempts >= 3:
                        st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                        st.experimental_rerun()
            else:
                st.error("⚠️ Data ID not found.")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        # Hardcoded master password for demo
        if login_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.logged_in = True
            st.success("✅ Reauthorized successfully! You may now retrieve your data.")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")
