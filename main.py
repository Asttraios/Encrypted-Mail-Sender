import gmail_config
import time
import os
import requests
import socket



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

    try:
        value= int(input("Enter your choice: "))
        user_decision(value)
    except:
        print("Invalid input! Please try again.")
        time.sleep(1)
        os.system('cls')
        menu()

def CheckInternetConnection(host="8.8.8.8", port=53, timeout=3):
    url = 'https://www.google.com/'
    
    
    while True:
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            print("Internet connection is established!")
            time.sleep(1)
            os.system('cls')
            return True

        except (socket.error, socket.timeout):
            print("No internet connection")
            time.sleep(1)
            os.system('cls')
            return False

menu()
