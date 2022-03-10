import requests
import json
from dictor import dictor


def author():
    print("+------------------+")
    print("| BIN Checker v1.0 |")
    print("| Author : Zeta    |") 
    print("+------------------+")
    print()

if __name__ == "__main__":
    author()

while True:

    def info():
        print()
        print ("[•] Network: " + str.capitalize(scheme))
        print ("[•] Type : " + str.capitalize(types))
        print ("[•] Brand : " + brand)
        print ("[•] Prepaid : " + prepaid)
        print ("[•] Bank : " + bank)
        print ("[•] Bank Phone Number : " + phone)
        print ("[•] Country : " + country)

    while True:
        try:
            a = str(input("Enter your BIN: "))
            print()
            b = a[:7]
            c = b.replace(" ", "")
            first = a[0]
            check = ['3','4','5','6']
            if (len(c) >= 6) and first in check:
                break
            else:
                print("Invalid Format, Please try again! \n")
        except IndexError:
            break

    url = f"https://lookup.binlist.net/{c}"
    try:
        result = requests.get(url)
        data = json.loads(result.text)
    except json.decoder.JSONDecodeError:
        break

    scheme = (str(dictor(data, 'scheme', default='Unknown')))
    types = (str(dictor(data, 'type', default='Unknown')))
    brand = (str(dictor(data, 'brand', default='Unknown')))
    prepaid = (str(dictor(data, 'prepaid', default='Unknown')))
    bank = (str(dictor(data, 'bank.name', default='Unknown')))
    phone = (str(dictor(data,'bank.phone', default='Unknown')))
    country = (str(dictor(data,'country.name', default='Unknown')))
    
    if __name__ == "__main__":
        info()
    print()
