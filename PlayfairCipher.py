

alphabet = "abcdefghiklmnopqrstuvwxyz"

            

def ReadyWord():                    #funkcja przygotowujaca klucz do wrzucenia do macierzy
   
   plain2 =""                       #klucz ktory zostanie wrzucony do macierzy, na pocz¹tku jest to pusty string

    
   plain = input("Enter an encrypting key: ")    #wprowadzenie przez uzytkownika klucza
   plain = str(plain)                               #zamiana na stringa na wszelki wypadek
   plain = plain.replace(" ", "")                   #usuniecie wszelkich spacji, zespawanie slow
   plain = plain.replace("j", "i")                  #wedlug schematu szyfru Playfaira powinno sie zastapic litery j na i
    
            
   for i in range (len(plain)):                     #petla przepisujaca pierwotny klucz do nowej zmiennej, tak aby zadna litera sie nie powtarzala
        if plain[i] not in plain2:
            plain2+=plain[i]      
   
   print(plain2)
               
   
   WordEnter(plain2)                                #przekazanie ostatecznego klucza do macierzy kodujacej 5x5


def WordEnter(plain):
    
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    count = 0                       #licznik kontroluj¹cy czy nie przekroczono dlugosci wprowadzonego slowa
    matrix = []
    new_row=[]
    new_alphabet=""
    

    
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

        
                
    #print(matrix)
    #return matrix                   #zwrot uzupelnionej macierzy 


ReadyWord()

    
    
    
    
    
    
