items={
    "baja taco":4.25,
    "burrito":7.50,
    "bowl":8.50,
    "nachos":11.00,
    "quesadilla":8.50,
    "pav baji":10.00,
    "pani puri":20.00,
    "chai":7.00,
    "biryani":100.0,
}
price=0
while True:
    y=str(input("Type your order:")).lower()
    if y in [""]:
        break
    elif y in items:
        price=price+items[y]
        print(f"price of item ${items[y]}")
        print(f"Total bill:{price}")
    else:
        print("Item not found")
       
print(f"Total bill:{price}")