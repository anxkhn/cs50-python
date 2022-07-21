def main():

    a, c, b = input("Enter: ").strip().split(" ")
    print(f"{calculate(int(a), str(c), int(b)):.1f}")


def calculate(a, c, b):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b


main()