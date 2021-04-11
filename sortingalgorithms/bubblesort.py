"""
Python bubblesort algorithms
"""


def bubbleSort(array):
    n = len(array)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def bubblesort():
    array = [54, 34, 35, 36, 1, 2, 0, 88, 25]
    print("Given array is", end="\n")
    printList(array)
    bubbleSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)


if __name__ == "__main__":
    bubblesort()
