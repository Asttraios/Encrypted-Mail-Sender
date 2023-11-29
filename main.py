import os
import gmail_config
import time

is_authorized = False

def user_decision(value, is_authorized):
    match value:
        case 1:
            #if(is_authorized == False):
                #print("Before you send anything, you must be authorized!")
                
                try:
                    gmail_config.user_authorization()       #tu taby trzeba poprawic, cofnac bo zakomentowalem ifa
                except:
                    print("Authorization unsuccessful")
                    time.sleep(2)
                    os.system('cls')
                    menu()
                    
                print("Authorization complete")
                #is_authorized = True
                
                gmail_config.mail_writeit()
                print("\n")
                user_confirm = input("Confirm? Y/N: ").strip().lower()
                
                if(user_confirm=='y'):
                    os.system('cls')      
                    print("Message ready to send!\n")
                    print("Building...\n")
                    gmail_config.mail_build()
                    print("E-Mail has been sent!\n Press any key to go back to menu...")
                    input()
                    menu()
                else:
                    #os.system('cls')
                    print("Discarding message...")
                    time.sleep(2)
                    menu()
        case 2:
            print("Encryption ")
        case 3:
            print("wyjscie")
        case _:
            print("zly wybor")
            
def menu():
    print("Welcome to MailToCipher, what would you like to perform?\n")
    print("1. Write a message\n")
    print("2. Encrypt the message\n")
    print("3. Exit\n")
    value= int(input("Enter your choice: "))
    user_decision(value, is_authorized)


menu()
