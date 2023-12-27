
from tkinter import WORD
import numpy as np


alphabet = "abcdefghiklmnopqrstuvwxyz"

            

def ReadyWord():                    #funkcja przygotowujaca klucz do wrzucenia do macierzy
   
   plain2 =""                       #klucz ktory zostanie wrzucony do macierzy, na poczatku jest to pusty string

    
   plain = input("Enter an encrypting key: ")    #wprowadzenie przez uzytkownika klucza
   plain = str(plain)                               #zamiana na stringa na wszelki wypadek
   plain = plain.replace(" ", "")                   #usuniecie wszelkich spacji, zespawanie slow
   plain = plain.replace("j", "i")                  #wedlug schematu szyfru Playfaira powinno sie zastapic litery j na i
    
            
   for i in range (len(plain)):                     #petla przepisujaca pierwotny klucz do nowej zmiennej, tak aby zadna litera sie nie powtarzala
        if plain[i] not in plain2:
            plain2+=plain[i]      
   
   print(plain2)
   
   return plain2
               
   


def WordEnter():
    
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    count = 0                       #licznik kontrolujacy czy nie przekroczono dlugosci wprowadzonego slowa
    matrix = []
    new_row=[]
    new_alphabet=""
    plain = ReadyWord()

    
    for i in range (5):             #stworzenie pustej macierzy 5x5
        for j in range (5):
            new_row.append('')
        matrix.append(new_row)      #dodanie wiersza (tablicy) do macierzy
        new_row=[]                  #nowy wiersz, uzupelniany pustymi stringami ""

    
    for i in range (len(alphabet)):
        if(alphabet[i] not in plain):
            new_alphabet+=str(alphabet[i])
            
    
    matrix_content = plain+new_alphabet

    print(matrix_content)
    
    for i in range (5):             # 5 wierszy macierzy      
       for j in range (5):          # 5-elementowy wiersz
            matrix[i][j] = matrix_content[count]
            count+=1         
    
    print(matrix)
    
    return matrix

    
    

def MessageReady():
    
    temp_matrix = WordEnter()
    temp_matrix=np.array(temp_matrix)
    secret_message=input("Write down your secret message: ")
    
    secret_message = secret_message.replace(" ", "")
    secret_message = secret_message.replace("j", "i")
    if(len(secret_message)%2!=0):
        print("nieparzyste")
        secret_message=secret_message+"x"
    
    message_to_receive=""

    for i in range (0, len(secret_message), 2):
        pair1=secret_message[i]
        pair2=secret_message[i+1]
        
        #print(np.where(temp_matrix == pair1))
        
        positionPair1 = np.where(temp_matrix == pair1)
        positionPair2 = np.where(temp_matrix == pair2)
        #print(position[0]) wiersze
        #print(position[1]) kolumny
        
        if(positionPair1[1] == positionPair2[1]):   #czy litery sa w tej samej kolumnie?
            #print("jest")
            pair1 = temp_matrix[(positionPair1[0]+1) % 5, (positionPair1[1]) % 5].astype(str).flatten()
            pair2 = temp_matrix[(positionPair2[0]+1) % 5, (positionPair2[1]) % 5].astype(str).flatten()
        elif(positionPair1[0] == positionPair2[0]):
            #print("jest")
            pair1 = temp_matrix[(positionPair1[0]) % 5, (positionPair1[1]+1) % 5].astype(str).flatten()
            pair2 = temp_matrix[(positionPair2[0]) % 5, (positionPair2[1]+1) % 5].astype(str).flatten()
        else:
            pair1 = temp_matrix[(positionPair1[0]) % 5, (positionPair2[1]) % 5].astype(str).flatten()
            pair2 = temp_matrix[(positionPair2[0]) % 5, (positionPair1[1]) % 5].astype(str).flatten()
        
        
        print(pair1)
        print(pair2)

        message_to_receive+=str(pair1) + str(pair2)
        
    print(secret_message[4])
    print(message_to_receive)
    return message_to_receive
    
if __name__ == "__main__":
    MessageReady()   
