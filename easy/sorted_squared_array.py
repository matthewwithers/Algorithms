"""
  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.
"""

array = [1, 2, 3, 5, 6, 8, 9]


def sortedSquaredArray(array):
    sqArr = [value**2 for value in array]
    sqArr.sort()
    return sqArr


print(sortedSquaredArray(array=array))
