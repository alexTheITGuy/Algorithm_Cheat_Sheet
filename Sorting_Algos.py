import random 

#Creates an unordered list of however many ints.
myIntList = []
number = 0

for i in range(100):
    random_integer = random.randint(1, 10)
    myIntList.append(random_integer)

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

#Menu to Select Algo to run... maybe later ill add run time information. 
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





