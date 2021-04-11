"""
Python heapsort algorithms
"""


# To heapify subtree rooted at index i.
# n is size of heap
def heapify(array, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left < n and array[i] < array[left]:
        largest = left

    # See if right child of root exists and is
    # greater than root
    if right < n and array[largest] < array[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # swap

        # Heapify the root.
        heapify(array, n, largest)


# The main function to sort an array of given size
def heapSort(array):
    n = len(array)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        heapify(array, i, 0)


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def heapsort():
    array = [54, 34, 35, 36, 1, 2, 0, 88, 25]
    print("Given array is", end="\n")
    printList(array)
    heapSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)


if __name__ == "__main__":
    heapsort()
