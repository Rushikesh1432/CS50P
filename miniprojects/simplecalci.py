operator=input("Enter (+ = * /): ")
x=int(input("Enter X:"))
y=int(input("Enter Y:"))
if operator=="+":
    print("Sum:",x+y)
elif operator=="-":
    print("Difference:",x-y)
elif operator=="*":
    print("Prd:",x*y)
elif operator=="/":
    print(f"{x/y}")