from cs50 import get_int

while True:
    height = get_int("Height: ")
# from cs50 2o21 fall
    if height > 0 and height < 9:
        for i in range(height):
            print(" " * (height - i - 1), end="")
            print("#" * (i + 1), end="")
            print()
        break
# different method than C