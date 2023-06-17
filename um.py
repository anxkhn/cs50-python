import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    x = re.findall("\b(um)\b",s)
    return x



if __name__ == "__main__":
    main()
