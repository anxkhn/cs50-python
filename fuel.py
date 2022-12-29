def main():
    val = get_val("What's x? ")
    print(val, end='')

def get_val(prompt):
    while True:
        x = input(prompt)
        if "/" in x:
            x = x.split("/")
            try:
                percent = round(int(x[0])/int(x[1])*100)
                #print(percent)
            except:
                pass
            if percent >= 99:
                return "F"
            elif percent <= 1:
                return "E"
            else:
                return (str(percent)+"%")
main()