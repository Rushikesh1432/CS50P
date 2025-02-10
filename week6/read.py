# with open("hi.txt","w") as file:
#     for i in range(3):
#         file.write(input("Enter:"))
#         file.write("\n")

list=[]

with open("hi.txt","r") as file:
    for line in file:
        name , house = line.rstrip().split(",")
        dic={"name":name,"house": house}
        list.append(dic)




for i in sorted(list,key=lambda s:s["house"],reverse=True):
    print(f"{i['name']} in {i['house']}")