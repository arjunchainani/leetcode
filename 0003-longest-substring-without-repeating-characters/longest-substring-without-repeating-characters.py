class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        currLen = 1
        longestLen = 1
        chars_map = {}

        # annoying edge case 
        if s == "":
            return 0

        chars_map[s[start]] = True

        while end < len(s) - 1:
            end += 1
            currLen += 1
            while s[end] in chars_map and end >= start:
                chars_map.pop(s[start])
                start += 1
                currLen -= 1
            
            if currLen > longestLen:
                longestLen = currLen
            
            chars_map[s[end]] = True

        return longestLen