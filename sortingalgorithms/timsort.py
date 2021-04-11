"""
Python timsort algorithms

1. Consider size of run as 32.
2. One by one sort pieces of size equal to run
3. After sorting individual pieces, merge them one by one.
    Double the size of merged subarrayays after every iteration.

"""
MIN_MERGE = 32


def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.

    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1  # same as [n / (2**1)]
    return n + r


# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(array, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


# Merge function merges the sorted runs
def merge(array, left, mid, right):

    # original arrayay is broken in two parts
    # left and right arrays
    len1, len2 = mid - left + 1, right - mid
    left_numbers, right_numbers = [], []
    for i in range(0, len1):
        left_numbers.append(array[left + i])
    for i in range(0, len2):
        right_numbers.append(array[mid + 1 + i])

    i, j, k = 0, 0, left

    # after comparing, we merge those two arrayay
    # in larger sub arrayay
    while i < len1 and j < len2:
        if left_numbers[i] <= right_numbers[j]:
            array[k] = left_numbers[i]
            i += 1

        else:
            array[k] = right_numbers[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        array[k] = left_numbers[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        array[k] = right_numbers[j]
        k += 1
        j += 1


def timSort(array):
    n = len(array)
    minRun = calcMinRun(n)

    # Sort individual subarrayays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(array, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:

        # Pick starting point of left sub arrayay. We
        # are going to merge array[left..left+size-1]
        # and array[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):

            # Find ending point of left sub arrayay
            # mid+1 is starting point of right sub arrayay
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub arrayay array[left.....mid] &
            # array[mid+1....right]
            if mid < right:
                merge(array, left, mid, right)

        size = 2 * size


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def timsort():
    array = [54, 34, 35, 36, 1, 2, 0, 88, 25]
    print("Given array is", end="\n")
    printList(array)
    timSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)


if __name__ == "__main__":
    timsort()
