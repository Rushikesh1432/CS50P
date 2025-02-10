from tabulate import tabulate
import sys

if len(sys.argv)>2:
  sys.exit("Too many arguments")
elif len(sys.argv)<2:
  sys.exit("Too few arguments")

try:
   file=open(sys.argv[1],"r")
except FileNotFoundError:
  sys.exit("File not found")

if not sys.argv[1].endswith(".csv"):
   sys.exit("File format error")

list=[]

for line in file:
    PIZZA,LARGE,SMALL=line.rstrip().split(",")
    sub=[PIZZA,LARGE,SMALL]
    list.append(sub)
    
print(tabulate(list,headers="firstrow",tablefmt="grid"))