import requests
import json
from dictor import dictor


print("+------------------+")
print("| BIN Checker v1.0 |")
print("| Author : Zeta    |") 
print("+------------------+")
print()


def info():
    print()
    print (f"[•] Network: {str.capitalize(scheme)}")
    print (f"[•] Type : {str.capitalize(types)}")
    print (f"[•] Brand : {brand}")
    print (f"[•] Prepaid : {prepaid}")
    print (f"[•] Bank : {bank}")
    print (f"[•] Bank Phone Number : {phone}")
    print (f"[•] Country : {country}")


while True:

    while True:
        try:
            bin_ = str(input("Enter your BIN: "))
            bin_number = bin_[:7]
            card_prefix = bin_[0]
            valid_prefix = ["3","4","5","6"]
            if (len(bin_number) >= 6) and card_prefix in valid_prefix:
                break
            else:
                print("\nInvalid Format, please try again!\n")
        except IndexError:
            break

    url = f"https://lookup.binlist.net/{bin_number}"

    try:
        result = requests.get(url)
        data = json.loads(result.text)
    except json.decoder.JSONDecodeError:
        break

    scheme = (str(dictor(data, "scheme", default="Unknown")))
    types = (str(dictor(data, "type", default="Unknown")))
    brand = (str(dictor(data, "brand", default="Unknown")))
    prepaid = (str(dictor(data, "prepaid", default="Unknown")))
    bank = (str(dictor(data, "bank.name", default="Unknown")))
    phone = (str(dictor(data,"bank.phone", default="Unknown")))
    country = (str(dictor(data,"country.name", default="Unknown")))

    if __name__ == "__main__":
        info()

    print()
