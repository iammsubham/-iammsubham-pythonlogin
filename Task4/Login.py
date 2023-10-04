import sqlite3
import hashlib

# Initialize the database
conn = sqlite3.connect("user_database.db")
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
conn.commit()

# Function to register a new user
def register_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

# Function to check if a user exists and the password is correct
def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    return cursor.fetchone() is not None

# Example registration and login
if __name__ == "__main__":
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
            print("User registered successfully!")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login_user(username, password):
                print("Login successful! Access granted.")
            else:
                print("Login failed! Invalid username or password.")

        elif choice == "3":
            break

# Close the database connection
conn.close()
