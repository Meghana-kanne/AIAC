import hashlib
import getpass

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(users_db):
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Please try another.")
        return
    password = getpass.getpass("Enter a new password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match.")
        return
    users_db[username] = hash_password(password)
    print("Registration successful.")

def login_user(users_db):
    username = input("Enter your username: ")
    if username not in users_db:
        print("Username not found.")
        return False
    password = getpass.getpass("Enter your password: ")
    if users_db[username] == hash_password(password):
        print("Login successful.")
        return True
    else:
        print("Incorrect password.")
        return False

def main():
    users_db = {}  # In-memory user database (username: hashed_password)
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            register_user(users_db)
        elif choice == '2':
            login_user(users_db)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
