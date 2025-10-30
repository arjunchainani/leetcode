# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# start at root node
# base case: both roots are None --> return None

# recursive case:
#   final_root = merge root nodes
#   final_root.left = mergeTrees(root1.left, root2.left)
#   final_root.right = mergeTrees(root1.right, root2.right)

# O(2 ^ log(larger_N)) = O(larger N) --> time complexity
# O(log(larger_N)) --> space complexity

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # base case
        if root1 is None and root2 is None:
            return None
        
        final_root = self.mergeNodes(root1, root2)
        if final_root is not None:
            merge_args = self.nullChecks(root1, root2, branch="left")
            final_root.left = self.mergeTrees(merge_args[0], merge_args[1])

            merge_args = self.nullChecks(root1, root2, branch="right")
            final_root.right = self.mergeTrees(merge_args[0], merge_args[1])

        return final_root

    def mergeNodes(self, root1, root2):
        # takes the two nodes and adds them up if both non-null, otherwise takes the non-null value
        final_root = TreeNode()
        if root1 is not None and root2 is not None:
            final_root.val = root1.val + root2.val
        elif root1 is not None:
            final_root.val = root1.val
        elif root2 is not None:
            final_root.val = root2.val
        else: # both roots are None
            return None
        
        return final_root

    def nullChecks(self, root1, root2, branch):
        # branch can either = "left" or "right"
        if root1 is not None and root2 is not None:
            return (root1.left, root2.left) if branch == "left" else (root1.right, root2.right)
        elif root1 is not None:
            return (root1.left, None) if branch == "left" else (root1.right, None)
        else:
            return (None, root2.left) if branch == "left" else (None, root2.right)

#              3
#          /        \
#         4          5
#      /     \    /     \
#     5 