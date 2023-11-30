

alphabet = "abcdefghiklmnopqrstuvwxyz"

def WordEnter(plain):
    column = 5
    row = 5
    count = 0
    help_count = 0
    matrix = []
    new_row=[]

    for i in range (5):
        for j in range (5):
            new_row.append('')
        matrix.append(new_row)
        new_row=[]

    print(matrix)
   
    '''
    row = 5
    count = 0
    help_count = 0
    matrix=[]
    new_row=[]
    
    while(len(plain)>help_count):
        if(count>=5 or (len(plain)-help_count)<5):
            matrix.append(new_row)
            new_row=[]
            count = 0
        new_row.append(plain[help_count])
        help_count+=1
        count+=1   
    print(matrix)
   ''' 
    for i in range (5):
       if(count>=len(plain)):
           break;
       for j in range (5):
            if(count<len(plain)):               
                matrix[i][j] = plain[count]
                count+=1
       
    return matrix
            

def ReadyWord():
   plain2 =""
   
   plain = input("Enter a word to encrypt it: ")
   plain = str(plain)
   plain = plain.replace(" ", "")
   plain = plain.replace("j", "i")
    
   for i in range (len(plain)):
       for j in range (i-1):
           if(plain[i]!=plain[j]):
               plain2+=plain[j]
             
   print(plain2)
       
   
   #if(plain[i-2]!=plain[j]):
             #plain2+=plain[i]

   #print(plain)
   #WordEnter(plain)


#result = WordEnter("bijatyka")
#print(result)

ReadyWord()

#def AlphabetFill(matrix):
    
    
    
    
    
    
