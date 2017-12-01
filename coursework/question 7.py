Sequence = [2,7,9,4,1,5,3,6,0,8]
CopySeq = Sequence[:]
def InsertionSort(x):
    print("Insertion Sort")
    for i in range(1,len(x)):
        key = x[i]
        j = i
        while j > 0 and x[j-1] > key:
            x[j] = x[j-1]
            j = j-1
            x[j] = key
            print(x)
            #return(x)
        

#InsertionSort(CopySeq)

def BubbleSort(x):
    print("Bubble Sort")
    length = len(x) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            print(x)
            if x[i] > x[i+1]:
                sorted = False
                x[i], x[i+1] = x[i+1], x[i]
                print(x)

            
BubbleSort(CopySeq)

def selectionSort(x):
    print("Selection Sort")
    for i in range (len(x)):
        minimum = min(x[i:])
        minIndex = x[i:].index(minimum)
        x[i + minIndex] = x[i]
        x[i] = minimum
        print(x)
        #return(x)


selectionSort(CopySeq)
