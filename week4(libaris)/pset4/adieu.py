names={}
while 1:
    name=str(input(""))

    if name in "quit" or "":
        break
    elif name not in names:
        names[name]=0
    names[name]+=1
    


    