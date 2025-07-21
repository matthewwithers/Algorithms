"""
  Write a function that takes in a sorted array of integers as well as a target
  integer. The function should use the Binary Search algorithm to determine if
  the target integer is contained in the array and should return its index if it
  is, otherwise -1
"""

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potential_match = array[middle]
    if target == potential_match:
        return middle
    elif target < potential_match:
        return binarySearchHelper(array, target, left, middle-1)
    else:
        return binarySearchHelper(array, target, middle+1, right)


print(binarySearch(array=array, target=target))
