class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        origNums1 = nums1[:m]
        i = 0 # pointer for nums1
        nums2Ptr = 0
        nums1Ptr = 0

        if m == 0:
            nums1[:n] = nums2[:n]
            return None
        if n == 0:
            return None
         
        while nums2Ptr < len(nums2) and nums2[nums2Ptr] <= origNums1[nums1Ptr]:
            nums1[i] = nums2[nums2Ptr]
            nums2Ptr += 1
            i += 1

        nums1[i] = origNums1[nums1Ptr]
        nums1Ptr += 1
        i += 1

        while (i < len(nums1)):
            if nums1Ptr >= len(origNums1) and nums2Ptr < len(nums2):
                nums1[i] = nums2[nums2Ptr]
                nums2Ptr += 1
                i += 1
                continue
            elif nums2Ptr >= len(nums2) and nums1Ptr < len(origNums1):
                nums1[i] = origNums1[nums1Ptr]
                nums1Ptr += 1
                i += 1
                continue
            
            if origNums1[nums1Ptr] <= nums2[nums2Ptr]:
                nums1[i] = origNums1[nums1Ptr]
                nums1Ptr += 1
            elif origNums1[nums1Ptr] > nums2[nums2Ptr]:
                nums1[i] = nums2[nums2Ptr]
                nums2Ptr += 1
            
            i += 1