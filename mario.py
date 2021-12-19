from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        for i in range(height):
            print(" " * (height - i - 1), end="")
            print("#" * (i + 1), end="")
            print()
        break
#different method than C , looked from cs50 lecture