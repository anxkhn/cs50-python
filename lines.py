import sys

len = len(sys.argv)
if len <= 1:
    print("Too few command-line arguments")
elif len>=3:
    print("Too many command-line arguments")
else:
    ext = sys.argv[1].split(".")
    if ext[1]!="py":
        print("Not a Python file")
    else:
        try:
            file = open(sys.argv[1],"r")
            lines = file.readlines()
            print(lines)
        except FileNotFoundError:
            sys.exit("File does not exist")
sys.exit()