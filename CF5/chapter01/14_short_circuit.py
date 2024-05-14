# short circuit

username = input("enter you username: ")
email = input("Enter you email : ")

valid_user = username or "User"

# print(valid_user)

print(f"Hello {valid_user}, " + ((email and f"your email is {email}") or ("please provide a valid emial address")))