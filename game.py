import random

while True:
    try:
        level = int(input("Level : "))
        num = random.randint(1, level)
    except:
        pass
    else:
        while True:
            try:
                x = int(input("Guess : "))
            except:
                pass
            else:
                if x>num:
                    print("Too large!")
                elif x<num:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
        break