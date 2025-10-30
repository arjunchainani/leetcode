# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# paths through the tree --> DFS traversal
# variable to keep track of maxPathElement = -10 ** 5
# variable to keep track of numGoodNodes = 0
# base case: if the tree only has one node, if node < maxPathElement --> not good node 
#                                             if node >= maxPathElement --> good node, increment numGoodNodes
# 
# recursive case: check if node to the left (if not None) is goodNode, check if node to the right (if not None) is goodNode, check if this node is a goodNode
#       -> maxPathElement -- scope of the path; passing this in as a function argument

# time complexity: O(N)
# space complexity: O(log N)

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxPathElement = -(10 ** 5)
        numGoodNodes = [0]

        self.findNumGoodNodes(root, maxPathElement, numGoodNodes)
        return numGoodNodes[0]
    
    def findNumGoodNodes(self, root, maxPathElement, numGoodNodes):        
        # check if the current node is a good node
        # update maxPathElement
        if root.val >= maxPathElement:
            numGoodNodes[0] += 1
            maxPathElement = root.val

        # base cases
        if root.left is None and root.right is None:
            return

        if root.left is not None:
            self.findNumGoodNodes(root.left, maxPathElement, numGoodNodes)
        
        if root.right is not None:
            self.findNumGoodNodes(root.right, maxPathElement, numGoodNodes)

# numGoodNodes = [1], maxPathElement = 3
#       - numGoodNodes = [2]
#   - numGoodNodes = [3], max = 4
#       - numGoodNodes = [4], max = 5