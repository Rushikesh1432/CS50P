import emoji

#take input from user
x=str(input("Enter:"))

#convert str to emoji format
emo=emoji.emojize(x,language='alias')
#print out final result
print(emo)