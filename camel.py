camelCase = input ("camelCase: ")
print("snake_case: ",end="")
for letter in camelCase:
    if letter.isupper():
        print("_" +  letter.lower(),end="")
    else:
        print(letter,end="")
print()