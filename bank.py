def main():
    input = input().strip().lower()
    print(f"${check(input)}")


def check(input):
    if input.startswith("hello"):
        return 0
    elif input.startswith("h"):
        return 20
    else:
        return 100


main()