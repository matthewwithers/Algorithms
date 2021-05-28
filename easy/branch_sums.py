"""
  Write a function that takes in a Binary Tree and returns a list of its branch
  sums ordered from leftmost branch sum to rightmost branch sum.


  A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
  branch is a path of nodes in a tree that starts at the root node and ends at
  any leaf node.

"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calBranchSums(root, 0, sums)
    return sums


def calBranchSums(node, runnningSum, sums):
    if node is None:
        return

    newRunningSum = runnningSum + node.value
    if node.left == None and node.right == None:
        sums.append(newRunningSum)
        return

    calBranchSums(node.left, newRunningSum, sums)
    calBranchSums(node.right, newRunningSum, sums)
