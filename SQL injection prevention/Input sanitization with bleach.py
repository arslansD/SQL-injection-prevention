import bleach

username = input("Enter a username: ")
password = input("Enter a password: ")

# Use bleach to sanitize the input
username = bleach.clean(username, strip=True)
password = bleach.clean(password, strip=True)

# Use the sanitized input in a SQL query
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"