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

#Menu to Select Algo to run
print('1 = Bubble Sort O(n^2)')
print('2 = Selection Sort O(n^2)')
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
        print('TODO')
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
