import hashlib

def hash_password(password):
    # Returns the SHA256 hash of the password string
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    # Get the stored password hash for the email, if it exists
    stored_hash = stored_logins.get(email)
    if stored_hash is None:
        # Email not found
        return False
    
    # Hash the password_to_check
    check_hash = hash_password(password_to_check)
    
    # Compare and return True if hashes match, False otherwise
    return stored_hash == check_hash

def main():
    # Example stored login data (email: password_hash)
    stored_logins = {
        "alice@example.com": hash_password("password123"),
        "bob@example.com": hash_password("qwerty"),
    }

    # Example usage
    email = input("Enter email: ")
    password = input("Enter password: ")

    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Login failed.")

if __name__ == '__main__':
    main()
