names=[]
for _ in range(3):
    names.append(input("enter:"))

names=sorted(names)
with open("hi.txt","a") as file:
    for i in range(3):
        file.write(f"{names[i]}\n")   