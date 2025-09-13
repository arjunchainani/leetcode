class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        matchingChars = True
        while matchingChars:
            curr_char = ""
            for string in strs:
                if i >= len(string) or (curr_char != "" and string[i] != curr_char):
                    matchingChars = False
                    return string[:i]
                
                else:
                    curr_char = string[i]
            
            i += 1
                    
        return string