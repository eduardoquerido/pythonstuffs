"""
Python insertionsort algorithms
"""


# Function to do insertion sort
def insertionSort(array):

    # Traverse through 1 to len(array)
    for i in range(1, len(array)):

        key = array[i]

        # Move elements of array[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def insertionsort():
    array = [54, 34, 35, 36, 1, 2, 0, 88, 25]
    print("Given array is", end="\n")
    printList(array)
    insertionSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)


if __name__ == "__main__":
    insertionsort()
