import inflect

p = inflect.engine()

names_list = []

while True:
    try:
        # Get user input
        name = input("Name(s): ")
        names_list.append(name)
    except EOFError:
        print()
        break
output = p.join(names_list)
print("Adieu, adieu, to "+ output)
