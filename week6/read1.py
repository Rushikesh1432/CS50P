with open("week6/names.txt","r") as file:
    for line in file:
        print(f"Hello,{line.rstrip()}")