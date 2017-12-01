Sequence = input("enter a sequence of number that you want to test")

def Reversedfun(seq):
    Reversed = seq[::-1]

    if Reversed == seq:
        print("yes")

    else:
        print("no")
Reversedfun(Sequence)
