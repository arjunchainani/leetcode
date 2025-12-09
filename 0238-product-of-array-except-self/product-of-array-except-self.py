# option 1: find total product and divide by each element -> NOT possible because we're not allowed to do the divide op
#
# option 2 (brute force): use python array slicing to grab all elements but the one you need (O(n^2) so doesn't work)
#
# option 3: using prefix and suffix products -> O(n)
# result[i] = prefix[i - 1] * suffix[i + 1] (1 if out of range)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        # loop 1: compute prefix product
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        # loop 2: compute suffix product
        suffix[-1] = nums[-1]
        for i in range(2, len(nums) + 1):
            suffix[-i] = suffix[-(i - 1)] * nums[-i]
        
        # loop 3: compute result
        result[0] = 1 * suffix[1]
        result[-1] = prefix[-2] * 1
        for i in range(1, len(result) - 1):
            result[i] = prefix[i - 1] * suffix[i + 1]
        
        return result