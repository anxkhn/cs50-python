def main():
    total = 0
    while(total<=50):
        print("Amount due:", 50-total)
        amount = int(input("Enter amount : ").strip())
        if amount == 50 or amount == 25 or amount == 10:
            total = total + amount
    print("Change owed: ",total-50)
main()