# LeetCode task: solving -> https://leetcode.com/problems/path-sum/description/
# 🦉 Preparation for coding interview 🍀

# Definition for a binary tree node.
# TreeNode class is defined to create a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # The constructor method to initialize the class members
        self.val = val
        self.left = left
        self.right = right

# Solution class is defined to solve the problem of the binary tree path sum


class Solution:
    # hasPathSum method is created to check if there is a path that sums up to the target sum
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # checking if the root node is None
        if not root:
            return False
        # checking if the root node is a leaf node
        if not root.left and not root.right:  # Leaf node
            return root.val == targetSum
        # subtracting the value of the current node from the target sum
        targetSum -= root.val
        # recursively calling the method for left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


# Creating the tree structure
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

# The target sum to be checked
targetSum = 22

# Creating an instance of Solution
solution = Solution()

# Calling the hasPathSum method to check if there is a path that sums up to the target sum
result = solution.hasPathSum(root, targetSum)

# Printing the result
print(result)
