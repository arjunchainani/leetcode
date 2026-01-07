# use monotonic stack for finding next greater element logic -> O(nums2.length)
# save each element and its greater element into a hash map, since elements are unique and you'll want to find them in linear time
# for generating answer, just iterate through nums1 and grab the value corresponding to that key from the hash map

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater_element = {}
        stack = []
        answer = []

        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                prev = stack.pop()
                next_greater_element[nums2[prev]] = nums2[i]
            
            stack.append(i)
        
        # for whatever's left in the stack, they don't have any matches -> map to -1
        for index in stack:
            next_greater_element[nums2[index]] = -1
        
        # use the hash map as a lookup table to construct the answer in linear time
        for i in range(len(nums1)):
            answer.append(next_greater_element[nums1[i]])
        
        return answer