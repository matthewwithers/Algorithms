
"""
  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.
"""

array = [141, 1, 17, -7, -17, -27, 18, 18, 541, 8, 7, 7]


def findThreeLargestNumbers(array):
    top_values = []
    for i in range(len(array)):
        cur_val = array[i]
        if len(top_values) < 3:
            top_values.append(cur_val)
        else:
            top_values.sort()
            if cur_val > top_values[0]:
                top_values[0] = cur_val
    top_values.sort()
    return top_values


print(findThreeLargestNumbers(array=array))
