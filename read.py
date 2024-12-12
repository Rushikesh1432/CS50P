
with open("hi.txt","r") as file:
    lines=file.readlines()
for line in sorted(lines):
    print(f"{line.strip()}")