# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        nodes = []
    
        def in_order_traversal(root):
            # left, root, right
            if root is None:
                return
            
            if root.left is not None:
                in_order_traversal(root.left)
            
            nodes.append(root.val)

            if root.right is not None:
                in_order_traversal(root.right)

        in_order_traversal(root)
        
        return nodes[k - 1]
