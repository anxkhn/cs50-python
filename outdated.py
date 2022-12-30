months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        # Split by /
        month, day, year = date.split("/")
        # month and date conditon check
        if (1<= int(month) <= 12) and (1 <= int(day) <= 31):
            break
    except:
        try:
            # Split by space
            o_month, o_day, year = date.split(" ")
            for i in range(len(months)):
                if o_month == months[i]:
                    month = i + 1
            day = o_day.replace(",","")
            if (1<= int(month) <= 12) and (1 <= int(day) <= 31):
                break
        except:
            pass
# print(year, end='')
# print("-", end='')
# if int(month) < 10:
#     print("0", end='')
# print(month, end='')
# print('-', end='')
# if int(day) < 10:
#     print("0", end='')
# print(day, end='')
print(f"{year}-{int(month):02}-{int(day):02}")