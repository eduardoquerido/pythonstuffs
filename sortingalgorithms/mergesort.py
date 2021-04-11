"""
Python mergesort algorithms
"""


def mergeSort(array):
    if len(array) > 1:

        # Finding the mid of the arrayay
        mid = len(array) // 2

        # Dividing the array elements into 2 halves
        L = array[:mid]
        R = array[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def mergesort():
    array = [54, 34, 35, 36, 1, 2, 0, 88, 25]
    print("Given array is", end="\n")
    printList(array)
    mergeSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)


if __name__ == "__main__":
    mergesort()
