import sys
import random
from pyfiglet import Figlet
figlet = Figlet()



if len(sys.argv) == 3:
    if sys.argv[1] == "--font" or sys.argv[1] == "-f":
        f = sys.argv[2]
        if f in figlet.getFonts():
            figlet.setFont(font=f)
            s = input("Enter Text : ")
            print(figlet.renderText(s))
        else:
            sys.exit("Error")
    else:
        sys.exit("Error")
elif len(sys.argv) == 1:
    s = input("Enter Text : ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(s))
else:
    sys.exit("Error")