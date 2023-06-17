import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return re.findall("\b(um\b)",s)



if __name__ == "__main__":
    main()
