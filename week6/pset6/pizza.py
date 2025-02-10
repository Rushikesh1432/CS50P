from tabulate import tabulate
list=[]
with open("regular1.csv","r") as file:
    for line in file:
     PIZZA,LARGE,SMALL=line.rstrip().split(",")
     sub=[PIZZA,LARGE,SMALL]
     list.append(sub)

print(tabulate(list,headers="firstrow",tablefmt="grid"))