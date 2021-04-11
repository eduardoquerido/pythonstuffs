"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1) Only one disk can be moved at a time.
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e.
    a disk can only be moved if it is the uppermost disk on a stack.
3) No disk may be placed on top of a smaller disk.

Python function to solve it
"""


def towerOfHanoi(number, source, destination, auxiliary):
    if number == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towerOfHanoi(number - 1, source, auxiliary, destination)
    print(f"Move disk {number} from {source} to {destination}")
    towerOfHanoi(number - 1, auxiliary, destination, source)


# number = number of disks
number = 5
towerOfHanoi(number, "A", "B", "C")
# A, C, B are the name of rods
