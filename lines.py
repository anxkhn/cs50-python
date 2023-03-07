import sys

def check_comment_or_empty_line(line):
    if line.lstrip().startswith('#'):
        return False
    if line.isspace():
        return False
    return True

len = len(sys.argv)
if len <= 1:
    sys.exit("Too few command-line arguments")
elif len>=3:
    sys.exit("Too many command-line arguments")
else:
    ext = sys.argv[1].split(".")
    if ext[1]!="py":
        sys.exit("Not a Python file")
    else:
        try:
            file = open(sys.argv[1],"r")
            lines = file.readlines()
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            count_lines = 0
            for line in lines:
                if check_comment_or_empty_line(line) == True:
                    count_lines += 1
            print(count_lines)

if __name__ == "__main__":
    main()