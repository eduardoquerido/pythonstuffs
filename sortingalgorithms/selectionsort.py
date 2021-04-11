"""
Python selectionsort algorithms
"""


def selectionSort(array):
    # Traverse through all array elements
    for i in range(len(array)):

        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        # Swap the found minimum element with
        # the first element
        array[i], array[min_index] = array[min_index], array[i]


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def selectionsort():
    array = [54, 34, 35, 36, 1, 2, 0, 88, 25]
    print("Given array is", end="\n")
    printList(array)
    selectionSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)


if __name__ == "__main__":
    selectionsort()
