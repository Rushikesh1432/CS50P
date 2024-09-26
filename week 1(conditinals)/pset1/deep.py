x = str(input("What is the to the great question of Life, the universe, and Everything? ")).strip().lower()

match x:
    case "forty-two" | "forty two" | "42":
        print("Yes")
    case _:
        print("No")