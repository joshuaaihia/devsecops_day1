# Blocklist of suspicious usernames
blocklist = ["admin", "root", "hacker"]

# Ask for a username
username = input("Enter your username: ")

# Security check
if username in blocklist:
    print("Access Denied: Suspicious login detected!")
else:
    print(f"Access Granted: Welcome {username}")

