name = input("What's your Name:")

match name:
    case "sai" | "rushi" | "sahil":
        print("road")
    case "karthik":
        print("house")
    case _:
        print("User not found")
        