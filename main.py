import time
import gmail_config
import os

is_authorized = False

def user_decision(value):
    match value:
        case 1:
            #try:    
                gmail_config.mail_build()
                print("Authorization complete!")
            #except:
                #print("Authorization unsuccessful!")
                #time.sleep(2)
                #os.system('cls')
                #menu()
        case 2:
            print("Encryption ")
        case 3:
            print("Wyjscie")
        case _:
            print("Zly wybor")
            
def menu():
    print("Welcome to MailToCipher, what would you like to perform?\n")
    print("1. Write a message\n")
    print("2. Encrypt the message\n")
    print("3. Exit\n")
    value= int(input("Enter your choice: "))
    user_decision(value)

menu()
