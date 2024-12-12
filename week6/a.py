for _ in range(10):
    name=input("enter:")
    with open("hi.txt","a") as file:
        file.write(f"{name}\n")