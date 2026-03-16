# BC: left > right return -1
# edge case: mid == left: return max(left if arr[left], right if arr[right])
# edge case: mid == right: return right

# if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1] then return mid
# if arr[mid] < arr[mid - 1] then search left half
# if arr[mid] < arr[mid + 1] then search right half

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # edge case 1
            if mid == left:
                return left if nums[left] > nums[right] else right
            # edge case 2
            if mid == right:
                return right

            # rest of the binary search
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid
            else:
                left = mid + 1
        
        return 0