import re

username = input("Enter a username: ")
password = input("Enter a password: ")

# Remove characters that could potentially alter the SQL query
username = re.sub(r'[;\'\"]', '', username)
password = re.sub(r'[;\'\"]', '', password)

query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
