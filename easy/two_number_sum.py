
"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.
"""


array = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

def twoNumberSum(array, targetSum):
    array.sort()
    for left in range(0, len(array)):
        for right in range(1, len(array)):
            comp = array[left] + array[right]
            if comp == targetSum:
                return [array[left], array[right]]
    return []


print(twoNumberSum(array=array,targetSum=target))