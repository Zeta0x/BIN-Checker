import requests
import json
import time


print("+------------------+")
print("| BIN Checker v1.1 |")
print("| Author : Zeta    |") 
print("+------------------+")
# print('https://www.youtube.com/watch?v=piz1IwsPd4w')


def countdown(timeout_sec):
    
    while timeout_sec:
        mins, secs = divmod(timeout_sec, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('Sleeping...' + timer, end="\r")
        time.sleep(1)
        timeout_sec -= 1


def check_is_digit(bin_):
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
    print_list = ['Network:', 'Type:', 'Brand:', 'Prepaid:', 'Bank:', 'Bank phone number:', 'Country:']
    for values, load_data in zip(print_list, data ):
        try:
            if load_data != 'Unknown':
                print(f'[+]{values} {load_data.capitalize()}')
            else:
                print(f'[-]{values} {load_data.capitalize()}')
        except AttributeError:
            if load_data != 'Unknown':
                print(f'[+]{values} {load_data}')
            else:
                print(f'[-]{values} {load_data}')
    print()


def get_bins():
    txt_bin_list = []
    try:
        with open('Bins.txt', 'r') as f:
            for i in f:
                line = i.strip()
                txt_bin_list.append(line)
    except FileNotFoundError:
        print('Bins.txt is not found!')
        with open('[+]Bins.txt', 'w') as f:
            print('[+]Creating Bins.txt file...')
            print('[+]Bins.txt created!')
    
    try:
        if txt_bin_list[0] == "":
            print('Bins.txt is empty!')
        else:
            return txt_bin_list
    except IndexError:
        print('Bins.txt is empty!')


def menu():
    
    print('\n[1] Single BIN lookup')
    print('[2] Mass BIN lookup')
    print('[0] Exit!')


def main(input_bin):
    try:
        check_int = check_is_digit(input_bin)
        bin_ = ''.join(check_int.split())
        bin_number = bin_[:7]
        card_prefix = bin_[0]
        valid_prefix = ['3','4','5','6']
        if (len(bin_number) >= 6):
            if card_prefix in valid_prefix:
                print(f'\nBIN: {bin_number}')
                url = f"https://lookup.binlist.net/{bin_number}"
                result = requests.get(url)
                status_code = result.status_code
                if status_code == 200:
                    data = json.loads(result.text)
                    fetch_data_list = fetch_info(data)
                    print_info(fetch_data_list)
                    return fetch_data_list
                elif status_code == 429:
                    print('Rate limited!')
                    countdown(60)
                elif status_code == 404:
                    print("BIN data doesn't exist!\n")
                else:
                    print('Something went wrong!\n')
            else:
                print("Invalid Format, please try again!\n")
        else:
            print("Invalid Format, please try again!\n")
    except IndexError:
        print("Invalid Format, please try again!\n")


def single_lookup():
    print('\nNote : Type [exit] to return to the menu!')
    while True:
        input_bin = str(input("Enter your BIN: "))
        if input_bin != 'exit':
            save_data = main(input_bin)
            if save_data:
                save_data.insert(0, input_bin)
                with open('Cached.txt', 'a') as data:
                    data.write(f'{save_data}\n')
        elif input_bin == 'exit':
            break
        
        

def mass_lookup():
    for input_bin in get_bins():
        save_data = main(input_bin)
        if save_data:
            save_data.insert(0, input_bin)
            with open('Cached.txt', 'a') as data:
                data.write(f'{save_data}\n')
    
    print('Options')
        

def options():
    while True:
        try:
            menu()
            option = int(input('\nEnter your option: '))
            if option == 0:
                break
            elif option == 1:
                single_lookup()
            elif option == 2:
                mass_lookup()
            else:
                print('Invalid option!')
                options()
        except ValueError:
            print('Invalid option!')
            options()
            

if __name__ == '__main__':
    options()
