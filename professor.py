import random


def main():
    level = get_level()
    score = level_checker(level)
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def math_checker(x,y):
    tries = 0
    while tries < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x+y):
                return 1
            else:
                tries += 1
                print("EEE")
        except:
            tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return 0

def level_checker(level):
    qno = 0
    score = 0
    while qno < 3:
        x,y = generate_integer(level)
        qno += 1
        print(qno)
        check = math_checker(x,y)
        if check == 1:
            score +=1
            print(score)
    return score

if __name__ == "__main__":
    main()