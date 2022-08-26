import requests
import json


print("+------------------+")
print("| BIN Checker v1.1 |")
print("| Author : Zeta    |") 
print("+------------------+\n")


def check_if_alpha(bin_):
    bin_list = []
    for i in bin_:
        if i.isdigit():
            bin_list.append(i)
        else:
            pass
        
    return_bin = str(''.join(bin_list))
    
    return return_bin


def fetch_info(data):
    return_data_list =[]
    req_bin_data = ['scheme', 'type', 'brand', 'prepaid']
    for i in req_bin_data:
        try:
            return_data_list.append(data[i])
        except KeyError:
            return_data_list.append('Unknown')
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
    print_list = ['Network:', 'Type :', 'Brand :', 'Prepaid :', 'Bank :', 'Bank phone number :', 'Country :']
    for annotation, print_data in zip(print_list, data ):
        try:
            if print_data != 'Unknown':
                print(f'[-]{annotation} {print_data.capitalize()}')
            else:
                print(f'[x]{annotation} {print_data.capitalize()}')
        except AttributeError:
            if print_data != 'Unknown':
                print(f'[-]{annotation} {print_data}')
            else:
                print(f'[x]{annotation} {print_data}')
    print()


def main():
    while True:
        try:
            input_bin = str(input("Enter your BIN: "))
            check_int = check_if_alpha(input_bin)
            bin_ = "".join(check_int.split())
            bin_number = bin_[:7]
            print(f'BIN: {bin_number}\n')
            card_prefix = bin_[0]
            valid_prefix = ["3","4","5","6"]
            if (len(bin_number) >= 6):
                if card_prefix in valid_prefix:
                    url = f"https://lookup.binlist.net/{bin_number}"
                    try:
                        result = requests.get(url).text
                        data = json.loads(result)
                        fetch_list_data = fetch_info(data)
                        print_info(fetch_list_data)

                    except json.decoder.JSONDecodeError:
                        print("Invalid Format, please try again!\n")
                else:
                    print("Invalid Format, please try again!\n")
            else:
                print("Invalid Format, please try again!\n")
        except IndexError:
            print("Invalid Format, please try again!\n")
            
            
if __name__ == '__main__':
    main()
