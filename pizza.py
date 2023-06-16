import sys
import csv
from tabulate import tabulate

def main():
    command_line_check()
    table = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(table[1:], table[0], tablefmt="grid"))

def command_line_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()