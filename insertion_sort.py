def InsertionSort(NumberList):
    n = len(NumberList)
    for j in range(1,n):
        key = NumberList[j]
        i=j-1
        while (i>=0 and NumberList[i]>key) :
            NumberList[i+1] = NumberList[i]
            i = i-1
        NumberList[i+1] = key
    return NumberList

#testList = [1,4,2,3,7,4,0]

#sortedList = InsertionSort(testList)
#print sortedList
