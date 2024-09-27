import sys
import pyfiglet

if len(sys)
if sys.argv[1] not in ["-f","-font"]:
    sys.exit("Error: Invalid argument")

x=str(input("Input:"))

if len(sys.argv)==0:
     sys.exit(pyfiglet.Figlet.renderText(x))



pyfiglet.Figlet.setFont(font=sys.argv[2])

print(pyfiglet.Figlet.renderText(x))


