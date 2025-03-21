
import numpy as np
import string
import re
    

def EncryptionKeyGenerate():

    
    encryption_key = input("Enter an encrypting key: ").lower()  # Wprowadzenie klucza przez u¿ytkownika
    
    # Usuwamy interpunkcjê, spacje i zamieniamy 'j' na 'i'
    encryption_key = re.sub(f"[{string.punctuation}]", "", encryption_key.replace(" ", "").replace("j", "i"))
    
                                                        
    encryption_key_ready = ""     
    
    for char in encryption_key:                       # Sprawdzamy czy litera nie wystêpuje ju¿ w kluczu
        if char not in encryption_key_ready:
            encryption_key_ready += char
    
    return encryption_key_ready
               
   


def MatrixAlphabetFill():
    
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    count = 0                       #licznik kontrolujacy czy nie przekroczono dlugosci wprowadzonego slowa
    matrix = []
    new_row=[]
    new_alphabet=""
    encryption_key = EncryptionKeyGenerate()

    
    for i in range (5):             #stworzenie pustej macierzy 5x5
        for j in range (5):
            new_row.append('')
        matrix.append(new_row)      #dodanie wiersza (tablicy) do macierzy
        new_row=[]                  #nowy wiersz, uzupelniany pustymi stringami ""

    
    for i in range (len(alphabet)):
        if(alphabet[i] not in encryption_key):
            new_alphabet+=str(alphabet[i])
            
    
    matrix_content = encryption_key+new_alphabet

    
    for i in range (5):             # 5 wierszy macierzy      
       for j in range (5):          # 5-elementowy wiersz
            matrix[i][j] = matrix_content[count]
            count+=1         
    
    
    return matrix

def PrepareSecretMessage(secret_message):

    secret_message = re.sub(f"[{string.punctuation}]", "", secret_message.lower().replace(" ", "").replace("j", "i"))

    processed_message = ""
    i = 0
    while i < len(secret_message):
        processed_message += secret_message[i]
        
        if i + 1 < len(secret_message) and secret_message[i] == secret_message[i + 1]:
            processed_message += "x"
        
        i += 1

    if len(processed_message) % 2 != 0:
        processed_message += "x"

    return processed_message    


def MessagePlayfairEncryption():
    
    temp_matrix = MatrixAlphabetFill()
    temp_matrix=np.array(temp_matrix)
    secret_message=input("Write down your secret message: ")
    
    secret_message = PrepareSecretMessage(secret_message)
    
    encrypted_message=""

    for i in range (0, len(secret_message), 2):
        pair1=secret_message[i]
        pair2=secret_message[i+1]
        
        
        positionPair1 = np.where(temp_matrix == pair1)
        positionPair2 = np.where(temp_matrix == pair2)

        
        if(positionPair1[1] == positionPair2[1]):   #czy litery sa w tej samej kolumnie?
            pair1 = temp_matrix[(positionPair1[0]+1) % 5, (positionPair1[1]) % 5].astype(str).item()
            pair2 = temp_matrix[(positionPair2[0]+1) % 5, (positionPair2[1]) % 5].astype(str).item()
        elif(positionPair1[0] == positionPair2[0]):
            pair1 = temp_matrix[(positionPair1[0]) % 5, (positionPair1[1]+1) % 5].astype(str).item()
            pair2 = temp_matrix[(positionPair2[0]) % 5, (positionPair2[1]+1) % 5].astype(str).item()
        else:
            pair1 = temp_matrix[(positionPair1[0]) % 5, (positionPair2[1]) % 5].astype(str).item()
            pair2 = temp_matrix[(positionPair2[0]) % 5, (positionPair1[1]) % 5].astype(str).item()
        
        
        encrypted_message+=pair1 +pair2
        
    return encrypted_message
    
if __name__ == "__main__":
    MessagePlayfairEncryption()   
