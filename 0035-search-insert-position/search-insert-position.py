class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(nums, value, left, right):
            if nums[(left + right) // 2] == value:
                return (left + right) // 2
            elif nums[left] == value:
                return left
            elif nums[right] == value:
                return right
            elif left + 1 == right or left == right:
                if nums[right] < value:
                    return right + 1
                elif nums[left] > value:
                    return 0
                else:
                    return right
            if value > nums[(left + right) // 2]:
                return binarySearch(nums, value, (left + right) // 2, right)
            elif value < nums[(left + right) // 2]:
                return binarySearch(nums, value, left, (left + right) // 2)
        
        return binarySearch(nums, target, 0, len(nums) - 1)