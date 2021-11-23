import requests

def menu():
    print("[1] Bin Lookup")
    print("[2] Option 2")
    print("[3] Option 3")
    print("[0] Exit the program")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:

        def info():
            print("[+] Network: " + str.capitalize(scheme))
            print("[+] Type : " + str.capitalize(type))
            print("[+] Brand : " + brand)
            print("[+] Prepaid : " + prepaid)
            print("[+] Bank : " + bank)

        while True:
            a = int(input("Enter your BIN: "))
            bin_no = str(a)
            first = bin_no[0]
            check = ['3','4','5','6']
            if (len(bin_no) >= 6) and first in check:
                break
            else:
                print("Invalid BIN length [" + str(len(bin_no)) + "] or Invalid Format, Please try again!")


        #Check if the length of bin is correct

        url = ('https://lookup.binlist.net/' + str(bin_no))
        payload = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }

        result = requests.get(url, payload).json()

        scheme = result['scheme']
        type = result['type']
        brand = result['brand']
        prepaid = str(result['prepaid'])
        bank = result['bank']['name']

        info()

    elif option == 2:
        print("you called option 2")
    elif option == 3:
        print("you called option 3")
    else:
        print("Invalid option")

    print()
    menu()
    
    option = int(input("Enter your option: "))

print("Thanks for using this program")