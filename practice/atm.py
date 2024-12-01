def main():
    total_amt=int(input("Enter Total amount:"))
    
    print("->1:Check balance")
    print("->2:Deposit money")
    print("->3:Withdraw money")
    print("->Any:Logout")
    

    while True:
        x=int(input("Enter:"))

        if(x==1):
            check(total_amt)
        elif(x==2):
            amt=int(input("Insert amt:"))
            total_amt=deposit(amt,total_amt)
            
            
        elif(x==3):
            amt=int(input("Enter amt to withdraw:"))
            total_amt = draw(amt,total_amt)
        else:
            print("logged out")
            break


def check(amt):
    print(f"Total Amount:{amt}")
def deposit(amt,total):
    t=amt+total
    print(f"Updated Amount:{t}")
    return t
def draw(amt,total):
    t=total-amt
    if(t>=0):
        print(f"Updated amount:{t}")
        return t
    else:
        print("Can't process\nplease check your aukat")

if __name__=="__main__":
    main()