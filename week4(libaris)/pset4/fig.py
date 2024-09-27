import sys
import pyfiglet

if sys.argv[1] not in ["-f","-font"]:
    sys.exit("Invalid argument")

x = str(input("Input:"))

figlet = pyfiglet.Figlet()

if sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid font")

print(figlet.renderText(x))