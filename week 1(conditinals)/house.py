name = input("What's your Name:").lower()

match name:
    case "sai" | "rushi" | "sahil":
        print("road")
    case "karthik" | "vikram":
        print("house")
    case _:
        print("User not found")
        