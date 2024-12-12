list=[]
with open("hi.csv","r") as file:
    for line in file:
        name,place=line.strip().split(",")
        # print(f"{name}:{place}")
        list.append(f"{name}:{place}")
for i in sorted(list):
    print(f"{i}")
