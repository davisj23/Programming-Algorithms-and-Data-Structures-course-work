test = input("type in the sentence you want to reverse ")

count = input("how many words ")
list1 = list(test)

def reverse(x ,y):
    x.extend(" ")
    counter = int(y)
    list2 = list()
    RevSeq = list()
    for k in x:
        if " " in k:
            RevSeq.extend(words(list2))
            RevSeq.extend(" ")
            list2 = list()
            print(RevSeq)
            counter -= 1
        elif counter  == 0:
            break
        
        else:
            list2.extend(k)
    del RevSeq[-1]
    return(RevSeq)
    



def words(segment):
    segment = segment[::-1]
    return(segment)
    

print(''.join(reverse(list1,count)))
