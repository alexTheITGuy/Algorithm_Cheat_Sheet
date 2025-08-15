import random 

#Creates an unordered list of however many ints.
myIntList = []
number = 0

for i in range(20):
    random_integer = random.randint(1, 10)
    myIntList.append(random_integer)

print(myIntList)
print()

#Bubble Sort
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):

            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    print(list)

#Selection Sort
def selection_sort(list):
    for scanIndex in range(0, len(list)):
        minIndex = scanIndex

        for compIndex in range(scanIndex + 1, len(list)):
            if list[compIndex] < list[minIndex]:
                minIndex = compIndex

        if minIndex != scanIndex:
                list[scanIndex], list[minIndex] = list[minIndex], list[scanIndex]

                print(list)

#Insertion Sort
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1

        while j>= 0 and key < list [j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    print(list)

#Merge Sort
def merge(list, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    #temp arrays for left and right
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = list[left + i]
    for j in range(n2):
        R[j] = list[mid + 1 + j]
    
    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        list[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        list[k] = R[j]
        j += 1
        k += 1

def merge_sort(list, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(list, left, mid)
        merge_sort(list, mid + 1, right)
        merge(list, left, mid, right)
    

#Menu to Select Algo to run
print('1 = Bubble Sort')
print('2 = Selection Sort')
print('3 = Insertion Sort')
print('4 = Merge Sort')
print('5 = Quick Sort')
print('6 = Heap Sort')
print('7 = Counting Sort')
print('8 = Radix Sort')
print('9 = Bucket Sort')
print('10 = Shell Sort')
print()

algo_selection = int(input('Select the algo to run: '))
match algo_selection :
    case 1:
        bubble_sort(myIntList)
    case 2:
        selection_sort(myIntList)
    case 3:
        insertion_sort(myIntList)
    case 4: 
        merge_sort(myIntList, 0, len(myIntList) - 1)
        print(myIntList)
        print()
    case 5:
        print('TODO')
    case 6:
        print('TODO')
    case 7:
        print('TODO')
    case 8:
        print('TODO')
    case 9:
        print('TODO')
    case 10: 
        print('TODO')
    case _:
        print('Please use a valid selection.')
