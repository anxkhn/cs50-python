def main():
    hello = input("Hi. ").strip().lower()
    print(f"${balance(hello)}")


def balance(hello):
    if hello.startswith("hello"):
        return 0
    elif hello.startswith("h"):
        return 20
    else:
        return 100


main()