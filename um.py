import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\b(um)\b",s, re.IGNORECASE))


if __name__ == "__main__":
    main()
