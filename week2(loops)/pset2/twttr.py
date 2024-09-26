x=str(input("Enter an word:"))

for i in range(len(x)):
    if x[i] in ["A","E","I","O","U","a","e","i","o","u"]:
        pass
    else:
        print(x[i],end="")
print()