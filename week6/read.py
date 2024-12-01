with open("week6/names.txt","r") as file:
    lines=file.readlines()

for _ in lines:
    print(f"hello,",_.rstrip())