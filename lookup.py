import requests
import json
from dictor import dictor


def menu():
    print("+------------------+")
    print("| BIN Checker v1.0 |")
    print("| Author : Zeta    |") 
    print("+------------------+\n")
menu()
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
        a = str(input("Enter your BIN: "))
        print()
        b = a[:7]
        c = b.replace(" ", "")
        first = a[0]
        check = ['3','4','5','6']
        if (len(c) >= 6) and first in check and (len(c) <= 16):
            break
        else:
            print("Invalid BIN length[" + str(len(c)) + "] or Invalid Format, Please try again! \n")

    url = ('https://lookup.binlist.net/' + (c))

    result = requests.get(url)
    data = json.loads(result.text)

    scheme = (str(dictor(data, 'scheme', default='Unknown')))
    types = (str(dictor(data, 'type', default='Unknown')))
    brand = (str(dictor(data, 'brand', default='Unknown')))
    prepaid = (str(dictor(data, 'prepaid', default='Unknown')))
    bank = (str(dictor(data, 'bank.name', default='Unknown')))
    phone = (str(dictor(data,'bank.phone', default='Unknown')))
    country = (str(dictor(data,'country.name', default='Unknown')))
        
    info()
    print()
