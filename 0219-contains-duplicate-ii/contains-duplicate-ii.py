class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        start = 0
        end = start + k

        curr_nums = {}
        for num in nums[start:end + 1]:
            if num in curr_nums:
                return True
            else:
                curr_nums[num] = True


        while start < len(nums) - 2 - k:
            curr_nums[nums[start]] = False
            start += 1
            end += 1
            if nums[end] in curr_nums and curr_nums[nums[end]] == True:
                return True
            else:
                curr_nums[nums[end]] = True
        
        # account for end of array edge case
        if end < len(nums) - 1: # if our window is not already at the end of the array
            curr_nums[nums[start]] = False
            start += 1
            if nums[-1] in curr_nums and curr_nums[nums[-1]] == True:
                return True

        return False 