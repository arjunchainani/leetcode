class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # edge case, n = 1
        if len(matrix) == 1:
            return matrix
        
        # step 1: transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # step 2: reverse
        for i in range(len(matrix)):
            matrix[i].reverse()

        return matrix