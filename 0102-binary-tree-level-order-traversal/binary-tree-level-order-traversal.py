# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        level_order_nodes = []
        curr_nodes = deque([root])

        while len(curr_nodes) != 0 and curr_nodes[0] != []:
            level_nodes = []
            level_values = []

            while len(curr_nodes) != 0:
                level_nodes.append(curr_nodes.popleft())
            
            for node in level_nodes:
                if node is not None:
                    level_values.append(node.val)
                    if node.left is not None:
                        curr_nodes.append(node.left)
                    if node.right is not None:
                        curr_nodes.append(node.right)
                    
            if len(level_values) > 0:
                level_order_nodes.append(level_values)
        
        return level_order_nodes