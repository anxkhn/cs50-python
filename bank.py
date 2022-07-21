def main():
    word = input().strip().lower()
    print(f"${check(word)}")


def check(word):
    if word.startswith("hello"):
        return 0
    elif word.startswith("h"):
        return 20
    else:
        return 100


main()