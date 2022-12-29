def main():
    val = get_val("What's x? ")
    print(val)

def get_val(prompt):
    while True:
        x = input(prompt)
        if "/" in x:
            x = x.split("/")
            try:
                frac = int(x[0])/int(x[1])
                #print(frac)
            except:
                pass
            if frac == 1:
                return "F"
            elif frac == 0:
                return "E"
            else:
                return (str(frac*100)+"%")
main()