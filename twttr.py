def main():
    string = input("Wht's yr nm? ")
    print("Output: ",end="")
    for letter in string:
        if not letter.lower() in ['a','e','i','o','u']:
            print(letter,end="")
print()
main()