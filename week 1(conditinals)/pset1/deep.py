#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

x = str(input("What is the to the great question of Life, the universe, and Everything? ")).strip().lower()

match x:
    case "forty-two" | "forty two" | "42":
        print("Yes")
    case _:
        print("No")