class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def monotonic_binary_search(left, right, arr):
            if left > right:
                return -1

            mid = (left + right) // 2                
            if mid == left:
                return min(arr[left], arr[right])

            if arr[mid] < arr[mid - 1]:
                return arr[mid]
            elif arr[mid] > arr[right]:
                return monotonic_binary_search(mid + 1, right, arr)
            else:
                return monotonic_binary_search(left, mid, arr)
    
        return monotonic_binary_search(0, len(nums) - 1, nums)
