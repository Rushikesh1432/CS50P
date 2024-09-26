import sys
#sys lib give ability to use argv 

if len(sys.argv)<2:
    sys.exit("Two few argv")   #sys.exit exits the program After printing string in it
elif len(sys.argv)>2: 
    sys.exit("Two many argv")

print("Hello ,",sys.argv[1])