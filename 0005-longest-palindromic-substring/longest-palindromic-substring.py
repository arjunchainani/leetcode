class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        M = [[0] * len(s) for _ in range(len(s))]
        palindromeInfo = [0, 1] # first index is for the starting index, second index is for length

        # base case 1
        for i in range(len(s)):
            M[i][i] = 1

        for L in range(2, len(s) + 1):
            for i in range(len(s) - L + 1):
                j = i + L - 1
                if getLongestPalindrome(s, M, i, j) and j - i + 1 >= palindromeInfo[1]:
                    palindromeInfo[1] = j - i + 1
                    palindromeInfo[0] = i
        
        return s[palindromeInfo[0]:palindromeInfo[0]+palindromeInfo[1]]

def getLongestPalindrome(word, M, i, j):
    if i == j:
        M[i][j] = 1
        return True
    elif (i + 1 == j) and word[i] == word[j]:
        M[i][j] = 1
        return True
    elif word[i] == word[j] and M[i+1][j-1] == 1:
        M[i][j] = 1
        return True
    else:
        return False

