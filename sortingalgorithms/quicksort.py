"""
Python heapsort algorithms

This function takes last element as pivot, places
the pivot element at its correct position in sorted
array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right
of pivot
"""


def partition(array, low, high):
    i = low - 1  # index of smaller element
    pivot = array[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if array[j] <= pivot:

            # increment index of smaller element
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


'''
The main function that implements QuickSort
array[] --> arrayay to be sorted,
low --> Starting index,
high --> Ending index

Function to do Quick sort
'''


def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:

        # pi is partitioning index, array[p] is now
        # at right place
        pi = partition(array, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def quicksort():
    array = [54, 34, 35, 36, 1, 2, 0, 88, 25]
    n = len(array)
    print("Given array is", end="\n")
    printList(array)
    quickSort(array, 0, n - 1)
    print("Sorted array is: ", end="\n")
    printList(array)


if __name__ == "__main__":
    quicksort()
