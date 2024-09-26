 #name error: giving a name to variable that we should'nt
def main():
    try:
        x=int(input("whats x:"))
    except ValueError:
        print("x is not integer")
    else:
        #break or
        print(f"x is {x}")



            #or
        #use break funtion in place of print(f"x is {x}")
main()