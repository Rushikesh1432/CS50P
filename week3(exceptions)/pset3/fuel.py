s=str(input("Fraction: ")).split("/")
try:
    x=int(s[0])
    y=int(s[1])
except ValueError or IndexError:
    print("Invalid input")
    
percent=int(round((x/y)*100))

if percent<=1:
    print("E")
elif percent>=99:
    print("F")
else:
    print(f"{percent}%")