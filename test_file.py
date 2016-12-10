from is_140422H import InsertionSort

def TestInsertionSort(NumberList):
    print 'Unsorted list : ', NumberList
    SortedList = InsertionSort(NumberList)
    print 'Sorted list : ', SortedList
    isSorted=True
    for i in range(0,len(SortedList)-1):
        if(SortedList[i]>SortedList[i+1]):
            isSorted=False
    if (set(NumberList)!=set(SortedList)):
        isSorted=False

    if (isSorted):
        print ("Answer is correct sorted list")
    else:
        print('Answer is not the correct sorted list')
    print
    return

list1 = [ 20, 12, 8, 5, 7, 10, 14]
list2 = [ 20, -7, 10, 14]
list3 = []
list4 = [0,0,0]

bigList=[list1, list2, list3, list4]

for lis in bigList:
    TestInsertionSort(lis)


#sort1=TestInsertionSort(list1)
#print sort1

