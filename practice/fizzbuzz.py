# FizzBuzz: Print numbers from 1 to 100, but for multiples of 3,
# print "Fizz" instead of the number, and for multiples of 5, print "Buzz".

def main():
    for i in range(1,101,1):
        
        if(i%3==0):
            print("Fizz,",end="")
        elif(i%5==0):
            print("Buzz,",end="")
        else:
            print(f"{i},",end="")








if __name__ == "__main__":
    main()



