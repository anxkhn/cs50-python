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
            except:
                pass
            else:
                if 99 <= percent <= 100:
                    return "F"
                elif 0<= percent <= 1:
                    return "E"
                elif 1<percent<99:
                    return (str(percent)+"%")
main()