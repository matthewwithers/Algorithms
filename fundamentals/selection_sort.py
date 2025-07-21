"""
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Selection Sort algorithm to sort the array.
"""


array = [8, 5, 2, 9, 5, 6, 3]


def selectionSort(array):
    for i, item in enumerate(array):
        min_indx = len(array) - 1
        for j in range(i, len(array)):
            if array[j] < array[min_indx]:
                min_indx = j

        if min_indx != i:
            array[min_indx], array[i] = array[i], array[min_indx]
    return array


print(selectionSort(array=array))
