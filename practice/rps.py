import random
def main():
    x=random.choice(["rock","paper","sissor"])
    user=0
    for i in range(3):
        while True:
            y=str(input("Enter:")).lower()
            if y in ["rock","paper","sissor"]:
                break
        if y=="rock" and x=="sissor":
            user+=1
        elif y=="paper" and x=="rock":
            user+=1
        if y=="sissor" and x=="paper":   
            user+=1

    if(user==3):
        print("You win")
    else:
        print("Computer wins")

if __name__ == "__main__":
    main()