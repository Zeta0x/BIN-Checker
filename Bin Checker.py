import requests
import json
from dictor import dictor


def menu():
    print("BIN Checker v1.0")
    print("Author : Zeta\n")

menu()

while True:

    def info():
        print()
        print ("[+] Network: " + str.capitalize(scheme))
        print ("[+] Type : " + str.capitalize(types))
        print ("[+] Brand : " + brand)
        print ("[+] Prepaid : " + prepaid)
        print ("[+] Bank : " + bank)
        print ("[+] Country : " + country)

    while True:
        a = str(input("Enter your BIN: "))
        first = a[0]
        check = ['3','4','5','6']
        if (len(a) >= 6) and first in check:
            break
        else:
            print("Invalid BIN length[" + str(len(a)) + "] or Invalid Format, Please try again!")

    url = ('https://lookup.binlist.net/' + (a))

    result = requests.get(url)
    data = json.loads(result.text)

    scheme = (str(dictor(data, 'scheme', default='Unknown')))
    types = (str(dictor(data, 'type', default='Unknown')))
    brand = (str(dictor(data, 'brand', default='Unknown')))
    prepaid = (str(dictor(data, 'prepaid', default='Unknown')))
    bank = (str(dictor(data, 'bank.name', default='Unknown')))
    country = (str(dictor(data,'country.name', default='Unknown')))
        
    info()
    print()
