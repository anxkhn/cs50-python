import sys
import random
from pyfiglet import Figlet
figlet = Figlet()



if len(sys.argv)== 3:
    if sys.argv[1] == "--font" or sys.argv[1] == "-f":
        s = input("Enter Text : ")
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(s))
elif len(sys.argv) == 1:
    s = input("Enter Text : ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(s))
else:
    sys.exit()