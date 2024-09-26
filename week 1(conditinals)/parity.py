def main():
    x = int(input("enter x:"))
    if if_even(x):
        print("x is even")
    else:
        print("x is not even")
    
def if_even(n):
    return n%2==0
    

main()