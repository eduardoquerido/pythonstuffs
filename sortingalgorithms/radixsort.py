"""
Python radixsort algorithms
"""


# A function to do the counting sort of array[] according to
# the digit represented by exp.
def sortCount(array, exp):

    n = len(array)

    # The output array elements that will have sorted array
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = array[i] / exp
        count[int(index % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output arrayay
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output arrayay
    i = n - 1
    while i >= 0:
        index = array[i] / exp
        output[count[int(index % 10)] - 1] = array[i]
        count[int(index % 10)] -= 1
        i -= 1

    # Copying the output arrayay to array[],
    # so that array now contains sorted numbers
    i = 0
    for i in range(0, len(array)):
        array[i] = output[i]


# Method to do Radix Sort
def radixSort(array):

    # Finding the number of digits
    max_length = max(array)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max_length / exp > 0:
        sortCount(array, exp)
        exp *= 10


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def radixsort():
    array = [54, 34, 35, 36, 1, 2, 0, 88, 25]
    print("Given array is", end="\n")
    printList(array)
    radixSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)


if __name__ == "__main__":
    radixsort()
