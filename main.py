import gmail_config
import time
import os
import requests



def user_decision(value):
    match value:
        case 1:
            try:    
                gmail_config.mail_build()
                os.system('cls')
                menu()
            except:
                print("Error! Contact the developer for help.")
                time.sleep(1)
                return 1
        case 2:
            #print("Wyjscie")
            return 1
        case _:
            print("Zly wybor")
            
def menu():
    
    CheckInternetConnection()

    print("Welcome to MailToCipher, what would you like to perform?\n")
    print("1. Write a message\n")
    print("2. Exit\n")
    value= int(input("Enter your choice: "))
    user_decision(value)
    

def CheckInternetConnection():
    url = 'https://www.google.com/'
    
    
    while True:
        try:
            x = requests.get(url)
            print("Status code: " + str(x.status_code))
            print("Internet connection is established!")
            time.sleep(1)
            os.system('cls')
            return 1
        except requests.ConnectionError:
            print("Status code: 404")
            print("No Internet connection!")
            time.sleep(1)
            os.system('cls')
            time.sleep(1)



menu()
