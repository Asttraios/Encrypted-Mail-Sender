import gmail_config
import time
import os


def user_decision(value):
    match value:
        case 1:
            try:    
                gmail_config.mail_build()
                os.system('cls')
                menu()
                print("flag!")
            except:
                #print("Unknown error! Contact the developer for help.")
                time.sleep(2)
                return 1
        case 2:
            print("Encryption ")
            return 1
        case 3:
            print("Wyjscie")
            return 1
        case _:
            print("Zly wybor")
            
def menu():
    print("Welcome to MailToCipher, what would you like to perform?\n")
    print("1. Write a message\n")
    print("2. Encrypt the message\n")
    print("3. Exit\n")
    value= int(input("Enter your choice: "))
    user_decision(value)
    
def clear():
     # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

menu()
