class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        powerset = []

        def dfs(path, position):
            if position == len(nums):
                powerset.append(path[:])
                return

            # case 1: don't add the number onto the path and recurse
            dfs(path, position + 1)

            # case 2: add the next number onto the path and recurse
            path.append(nums[position])
            dfs(path, position + 1)
            path.pop()

        dfs(path, 0)
        return powerset