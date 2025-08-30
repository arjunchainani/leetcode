# not the most optimal way, but still O(n) time complexity 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_map = {}
        for number in nums:
            sum_map[number] = target - number

        for key in sum_map.keys():
            if (sum_map[key] in sum_map.keys()) and (sum_map[sum_map[key]] == key):
                num1 = key
                num2 = sum_map[key]
        
        index1 = nums.index(num1)
        if num1 == num2:
            nums[index1] = None
        
        index2 = nums.index(num2)
        return [index1, index2] 