import re
import sys
from validator_collection import is_email


def main():
    print(check(input("What's your email address? ")))

def check(s):
    if is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
