word1 = input('type in the first word ') 
word2 = input('type in the second word ') 
counter = 0 
list1 = list() 
word1 = list(word1) 
word2 = list(word2)


while len(word1)>counter or len(word2)>counter:
    if len(word1)>counter and len(word2)>counter:
        list1.extend(word1[counter]+word2[counter])
        counter+=1
        
    elif len(word1)>counter and len(word2)<=counter:
        leftover = counter - len(word1)
        list1.extend(word1[leftover:])
        break
    
    elif len(word2)>counter and len(word1)<=counter:
        leftover = counter - len(word2)
        list1.extend(word2[leftover:])
        break
    

combineStr = ''.join(list1) #converts the list into a string
print(combineStr)
