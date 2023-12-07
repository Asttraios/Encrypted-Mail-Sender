

alphabet = "abcdefghiklmnopqrstuvwxyz"

def WordEnter(plain):
    column = 5
    row = 5
    count = 0                       #licznik kontroluj¹cy czy nie przekroczono dlugosci wprowadzonego slowa
    matrix = []
    new_row=[]

    for i in range (5):             #stworzenie pustej macierzy 5x5
        for j in range (5):
            new_row.append('')
        matrix.append(new_row)      #dodanie wiersza do macierzy
        new_row=[]                  #nowy wiersz, uzupelniany pustymi stringami ""

    print(matrix)                   #kontrolne wypisanie "pustej" tablicy
   

    for i in range (5):             # 5 wierszy macierzy
       if(count>=len(plain)):       #jesli licznik przekroczy dlugosc slowa to petla sie przerywa
           break;                   
       for j in range (5):          # 5-elementowy wiersz
            if(count<len(plain)):   #warunek: na wypadek gdyby nie dalo sie w pelni uzupelnic wiersza i bedzie wypelniony po czesci (bedzie mniej niz 5 liter w jednym wierszu)            
                matrix[i][j] = plain[count]
                count+=1
    print(matrix)
    return matrix                   #zwrot uzupelnionej macierzy 
            

def ReadyWord():                    #funkcja przygotowujaca klucz do wrzucenia do macierzy
   
   plain2 =""                       #klucz ktory zostanie wrzucony do macierzy

    
   plain = input("Enter a word to encrypt it: ")    #wprowadzenie przez uzytkownika klucza
   plain = str(plain)                               #zamiana na stringa na wszelki wypadek
   plain = plain.replace(" ", "")                   #usuniecie wszelkich spacji, zespawanie slow
   plain = plain.replace("j", "i")                  #wedlug schematu szyfru Playfaira powinno sie zastapic litery j na i
    
            
   for i in range (len(plain)):                     #petla przepisujaca pierwotny klucz do nowej zmiennej, tak aby zadna litera sie nie powtarzala
        if plain[i] not in plain2:
            plain2+=plain[i]      
   
   print(plain2)
               
   
   WordEnter(plain2)                                #przekazanie ostatecznego klucza do macierzy


ReadyWord()

    
    
    
    
    
    
