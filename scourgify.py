import sys


def main():
    check_command_line_arg()
    output = []
    # Try to open the file
    sys.argv[1]
    try:
        file1 = open(sys.argv[1])
        read_content = file1.readlines()
        file1.close()

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Write new csv file
    with open(sys.argv[2], "w") as file:
        for i in read_content:
            x = i.replace(" ","").replace('"', "")
            file.write(x)
            file.write("\n")


def check_command_line_arg():
    # Check how many elements in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Check if it is a CSV file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
