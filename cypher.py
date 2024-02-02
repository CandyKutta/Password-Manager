import string
import random

choice= int(input("Do you wanna 1.Cypher or 2.Decypher the code?\n"))

if(choice==1):
    
    words = input("Enter your word to cypher\n")
    word= words.split(" ")
    cypher=[]
    for i in word:
        if(len(i)<=3):
        #cypher.append(word[::-1])
       # print(" ".join(cypher))
            
            #print(i[::-1])
            cypher.append(i[::-1])

        else:
            
            ran=''.join((random.choices(string.ascii_letters+string.digits,k=4)))
            
    
            encode=ran + i[1:]+i[0] + ran
    
            
           
            cypher.append(encode)
    print(" ".join(cypher))
        
elif(choice==2):
    words = input("Enter your word to decypher!\n")
    word= words.split(" ")
    cypher=[]
    for i in word:
        if(len(i)<=3):
        #cypher.append(word[::-1])
       # print(" ".join(cypher))
            
            #print(i[::-1])
            cypher.append(i[::-1])

        else:
            
            
            
    
            decode= i[4:-4] 
            decode= decode[-1]+decode[:-1]
         
    
            
           
            cypher.append(decode)
    print(" ".join(cypher))
    
else:
    print("Invalid Input!")
    
    
    
  
        
    
    