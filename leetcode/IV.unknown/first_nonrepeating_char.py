
"""
  Write a function that takes in a string of lowercase English-alphabet letters
  and returns the index of the string's first non-repeating character.
"""

s = 'abcdcaf'


def firstNonRepeatingCharacter(string):
    stringArray = list(string)
    filteredValues = [
        letter for letter in stringArray if stringArray.count(letter) == 1]
    if len(filteredValues) == 0 or stringArray == set(stringArray):
        return -1
    return stringArray.index(filteredValues[0])


print(firstNonRepeatingCharacter(string=s))
