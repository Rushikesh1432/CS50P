name=input("Enter:")

with open("week6/names.txt","a") as file:
    file.write(f"{name}\n")



