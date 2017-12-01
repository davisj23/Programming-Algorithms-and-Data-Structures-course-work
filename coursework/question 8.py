

def BinarySearch(x):
    top = 0
    bottem = len(x)

    check = False
    while check is not True:
        p = (top + bottem) // 2
        guess = p
        print(guess)
        reply = input(" is this your number Yes/Higher/Lower")
        reply = list(reply)
        
        if ("y") or ("Y") or ("Yes") or ("yes") in reply:
            print("your number is")
            return p
            #check = True
            
        elif ("h") or("H") or ("Higher") or ("higher") in reply:
            bottem = p
            
        elif ("l") or ("L") or ("Lower") or ("lower") in reply:
            top = p
            print("third")

            
array = list(range(0, 20000))

print(BinarySearch(array))
