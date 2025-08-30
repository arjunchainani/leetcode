class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            nums[i] = nums[j]
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            
            i += 1
        
        return i