def main():
    val = get_val("What's x? ")
    print(val, end='')

def get_val(prompt):
    while True:
        x = input(prompt)
        if "/" in x:
            x = x.split("/")
            try:
                frac = int(x[0])/int(x[1])*100
                #print(frac)
            except:
                pass
            if frac >= 99:
                return "F"
            elif frac <= 1:
                return "E"
            else:
                return (str(frac*100)+"%")
main()