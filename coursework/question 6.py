def LinearSearch(sequence,x):
    for k in sequence:
        if int(k) == int(x):
            return("yes")
    return("no")

L = [3,5,7,1,2,9]
List1 = input("enter the list of numbers that you want to search though ")

Target = input("what is the number you want to check for ")

print(LinearSearch(List1,Target))
