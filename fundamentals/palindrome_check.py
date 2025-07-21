"""
  Write a function that takes in a non-empty string and that returns a boolean
  representing whether the string is a palindrome.
"""


s = 'abcdcba'


def isPalindrome(string):
    return string[::-1] == string


print(isPalindrome(s))
