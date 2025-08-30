# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        curr_nodes1 = deque([p])
        curr_nodes2 = deque([q])

        while len(curr_nodes1) != 0:
            curr_node1 = curr_nodes1.popleft()
            curr_node2 = curr_nodes2.popleft()

            if curr_node1 is None and curr_node2 is None:
                continue
            elif (curr_node1 is None) or (curr_node2 is None):
                return False
            elif (curr_node1.val != curr_node2.val):
                return False
            else:
                curr_nodes1.append(curr_node1.left)
                curr_nodes1.append(curr_node1.right)
                curr_nodes2.append(curr_node2.left)
                curr_nodes2.append(curr_node2.right)
        
        return True
