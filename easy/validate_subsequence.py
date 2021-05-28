
"""
Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.
"""


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def isValidSubsequence(array, sequence):
    arrIndex, seqIndex = 0, 0
    while arrIndex < len(array) and seqIndex < len(sequence):
        if array[arrIndex] == sequence[seqIndex]:
            seqIndex += 1
        arrIndex += 1
    # did we finish finding all the matching values?
    return seqIndex == len(sequence)


print(isValidSubsequence(array=array,sequence=sequence))