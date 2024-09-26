def main():
    n  = int(input("How many liters:"))
    paal(n)




def paal(a):   
    try:
        if a > 0:
            x=70*a
            print(f"Price for {a} liters in {x}")
    except ValueError:
        print("Invalid input")