# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursively invert subtrees until we hit a base case
# base cases: 1) if root == null; return and backtrack
# recursive case: swap the left and right node, then invert left and right subtree
# time complexity: O(N)
# space complexity: O(N)

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # base case
        if root == None:
            return None
        
        # swap + recursive case 
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root