names=[]
for _ in range(3):
    name=str(input("Enter:"))
    names.append(name)
print()
for _ in sorted(names):
    print(f"Hello,{_}")