import requests
import sys

if len(sys.argv) == 2:
    pass
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument ")
    sys.exit(1)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    amount = response['bpi']['USD']['rate_float'] * value
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("RequestException Occured")
    sys.exit(1)
