#value error 
#if we input string or any other than integer w'll get value error

#x=int(input("What's x?"))
#print(f"x is {x}")

#solution of this
try:
    n=int(input("Whats n?"))
    print(f"n is {n}")
except ValueError:
    print("x is not interger")

