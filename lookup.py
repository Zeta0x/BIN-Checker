import requests
import json
import colorama
from dictor import dictor
from colorama import Fore

colorama.init(autoreset = True)
def menu():
    print(f"{Fore.GREEN} +------------------+")
    print(f"{Fore.GREEN} | BIN Checker v1.0 |")
    print(f"{Fore.GREEN} | Author : Zeta    |") 
    print(f"{Fore.GREEN} +------------------+\n")
menu()

while True:

    def info():
        print()
        print (f"{Fore.GREEN}[•] Network: " + str.capitalize(scheme))
        print (f"{Fore.GREEN}[•] Type : " + str.capitalize(types))
        print (f"{Fore.GREEN}[•] Brand : " + brand)
        print (f"{Fore.GREEN}[•] Prepaid : " + prepaid)
        print (f"{Fore.GREEN}[•] Bank : " + bank)
        print (f"{Fore.GREEN}[•] Bank Phone Number : " + phone)
        print (f"{Fore.GREEN}[•] Country : " + country)

    while True:
        a = str(input("Enter your BIN: "))
        b = a.strip()
        first = a[0]
        check = ['3','4','5','6']
        if (len(b) >= 6) and first in check and (len(b) <= 16):
            break
        else:
            print(f"\n{Fore.RED}Invalid BIN length[" + str(len(b)) + "] or Invalid Format, Please try again! \n")

    url = ('https://lookup.binlist.net/' + (b))

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
