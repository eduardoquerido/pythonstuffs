from bubblesort import bubblesort
from heapsort import heapsort
from insertionsort import insertionsort
from mergesort import mergesort
from quicksort import quicksort
from radixsort import radixsort
from selectionsort import selectionsort
from timsort import timsort

from timeit import default_timer as timer

# BubbleSort
start = timer()
bubblesort()
end = timer()
bubblesort_elapsed_time = end - start

# HeapSort
start = timer()
heapsort()
end = timer()
heapsort_elapsed_time = end - start

# InsertionSort
start = timer()
insertionsort()
end = timer()
insertion_elapsed_time = end - start

# MergeSort
start = timer()
mergesort()
end = timer()
mergesort_elapsed_time = end - start

# QuickSort
start = timer()
quicksort()
end = timer()
quicksort_elapsed_time = end - start

# RadixSort
start = timer()
radixsort()
end = timer()
radixsort_elapsed_time = end - start

# SelectionSort
start = timer()
selectionsort()
end = timer()
selectionsort_elapsed_time = end - start

# TimSort
start = timer()
timsort()
end = timer()
timsort_elapsed_time = end - start

print(f"Elapsed time for bubblesort: {bubblesort_elapsed_time}")
print(f"Elapsed time for heapsort: {heapsort_elapsed_time}")
print(f"Elapsed time for insertionsort: {insertion_elapsed_time}")
print(f"Elapsed time for quicksort: {quicksort_elapsed_time}")
print(f"Elapsed time for radixsort: {radixsort_elapsed_time}")
print(f"Elapsed time for selectionsort: {selectionsort_elapsed_time}")
print(f"Elapsed time for timsort: {timsort_elapsed_time}")
