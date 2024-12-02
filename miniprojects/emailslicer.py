email=str(input("Enter email: "))
index=email.index("@")
username=email[:index]
domain=email[index:]
print(f"Username is {username} and domain is {domain}")

