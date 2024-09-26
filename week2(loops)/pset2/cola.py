change_owend = 50

if change_owend>0:
    print(f'change owned is {change_owend}')

coin = int(input("Insert coin:"))

if coin in [50,25,10,5,0]:
    change_owend = change_owend-coin
    print(f'change owned {change_owend}')


          
