#dictionary
list = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
# Loop forever
while True:
    try:
        item = input("Item: ").title()
        if item in list:
            total = total + list[item]
            print(f"Total: $",end='')
            print('%.2f' % total)
    except EOFError:
        print()
        break