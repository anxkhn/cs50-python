def main():
    fruit = str(input("Enter Fruit Name : ").strip().lower())
    if "apple" in fruit:
        print("Calories: 130")
    elif "avocado" in fruit:
        print("Calories: 50")
    elif "sweet cherries" in fruit:
        print("Calories: 100")

main()