groceries={}

while True:
    item  =str(input("Enter:"))
    if  item == "quit" or " ":
        break
    elif item not in groceries:
        groceries[item]=0

    groceries[item] += 1

keys=list(groceries.keys())

keys.sort()
        
for k in keys:
    print(f"{groceries[k]} {k.upper()}  ")
