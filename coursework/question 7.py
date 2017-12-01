Sequence = [2,7,9,4,1,5,3,6,0,8]
CopySeq = Sequence[:]

def InsertionSort(x):
    print("Insertion Sort")
    ElementCount = 0
    ComparisonCount = 0
    for i in range(1,len(x)):
        ComparisonCount += 1
        key = x[i]
        j = i
        while j > 0 and x[j-1] > key:
            ElementCount += 1
            x[j] = x[j-1]
            j = j-1
            x[j] = key
            print(x)
            #return(x)
    print(ElementCount)
    print(ComparisonCount)


#InsertionSort(CopySeq)

def BubbleSort(x):
    ElementCount = 0
    ComparisonCount = 0

    print("Bubble Sort")
    length = len(x) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            ComparisonCount +=1
            if x[i] > x[i+1]:
                ElementCount += 1
                sorted = False
                x[i], x[i+1] = x[i+1], x[i]
                print(x)
    print(ElementCount)
    print(ComparisonCount)


            
#BubbleSort(CopySeq)

def selectionSort(x):
    ElementCount = 0
    ComparisonCount = 0

    print("Selection Sort")
    for j in range (len(x)):
                     #https://stackoverflow.com/questions/15235264/selection-sort-python
                    #used this code to help me do a selection algoritum
        x[j] = lowest
        bottemInd = x[j:].index(lowest)
        x[j + bottemInd] = x[j]
        lowest = min(x[j:])
        print(x)
        ElementCount += 1
        ComparisonCount += 1
    print(ElementCount)
    print(ComparisonCount)
    
        #return(x)

selectionSort(CopySeq)
