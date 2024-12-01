names=[]

with open("week6/names.txt") as file:
    for line in file:
        names.append(line)

for name in sorted(names):
    print(f"Hello,{name.rstrip()}")