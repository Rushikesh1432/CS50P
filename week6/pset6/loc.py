import sys

if len(sys.argv)>2:
    sys.exit("Too many arguments")
elif len(sys.argv)<2:
    sys.exit("Too few arguments")

if ".py" not in sys.argv[1]:
    sys.exit("mention file type")
x=0
try:
    file=open(sys.argv[1],"r")
except FileNotFoundError:
    sys.exit("File not found")
              

    
for l in file.read().splitlines():
    if len(l.strip())==0:
        pass
    elif l.strip().startswith("#"):
         pass
    else:
        x=x+1
        
print(x)