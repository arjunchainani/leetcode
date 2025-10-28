class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        path = []

        def dfs(path, candidates, start):
            if target - sum(path) < 0:
                return
            elif target - sum(path) == 0:
                combinations.append(path[:])
                return

            # try adding candidates[i] to path - use start to avoid situations where you're reconsidering something 
            # you already considered earlier in your state-space tree, therefore avoiding duplicates
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(path, candidates, i)
                path.pop()

        dfs(path, candidates, 0)
        return combinations