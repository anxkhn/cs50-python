def main():
    a, b = input("Enter the time: ").strip().split(":")

    z = convert(int(a),int(b))
    if z >= 7.0 and z <= 8.0:
        print("breakfast time")
    elif z >= 12.0 and z <= 13.0:
        print("lunch time")
    if z >= 18.0 and z <= 19.0:
        print("dinner time")


def convert(a,b):
    b = float(b/60)
    z = float(a + b)
#   if c == "p.m.":
#       z = z + 12
    return z


if __name__ == "__main__":
    main()