import requests
import json


print("+------------------+")
print("| BIN Checker v1.1 |")
print("| Author : Zeta    |") 
print("+------------------+\n")


def fetch_info(data):
    return_data_list =[]
    req_bin_data = ['scheme', 'type', 'brand', 'prepaid']
    for i in req_bin_data:
        try:
            return_data_list.append(data[i])
        except KeyError:
            return_data_list.append('unknown')
    try:
        return_data_list.append(data['bank']['name'])
    except KeyError:
        return_data_list.append('Unknown')
        
    try:
        return_data_list.append(data['bank']['phone'])
    except KeyError:
        return_data_list.append('Unknown')
        
    try:
        return_data_list.append(data['country']['name'])
    except KeyError:
        return_data_list.append('Unknown')
        
    return return_data_list


def print_info(data):
    print_list = ['[•] Network:', '[•] Type :', '[•] Brand :', '[•] Prepaid :', '[•] Bank :', '[•] Bank phone number :', '[•] Country :']
    for a, b in zip(print_list, data ):
        try:
            print(f'{a} {b.capitalize()}')
        except AttributeError:
            print(f'{a} {b}')
    print()

while True:
    try:
        bin_ = str(input("Enter your BIN: "))
        bin_ = "".join(bin_.split())
        bin_number = bin_[:7]
        card_prefix = bin_[0]
        valid_prefix = ["3","4","5","6"]
        if (len(bin_number) >= 6):
            if card_prefix in valid_prefix:
                url = f"https://lookup.binlist.net/{bin_number}"
                try:
                    result = requests.get(url).text
                    data = json.loads(result)
                    fetch_list_data = fetch_info(data)
                    if __name__ == '__main__':
                        print_info(fetch_list_data)

                except json.decoder.JSONDecodeError:
                    print("Invalid Format, please try again!\n")
            else:
                print("Invalid Format, please try again!\n")
        else:
            print("Invalid Format, please try again!\n")
    except IndexError:
        print("Invalid Format, please try again!\n")
