class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        transposedZigzag = []
        horizontalLetters = [[] for i in range(numRows)]

        if len(s) <= numRows:
            return s

        index = 0 
        while index < len(s):
            # there's going to be issues with edge cases that have words smaller than numRows
            init_chunk = list(s[index:index + numRows])
            transposedZigzag.append(init_chunk)
            for i, char in enumerate(init_chunk):
                horizontalLetters[i].append(char)
                
            index += numRows

            if index >= len(s):
                break

            rightOffset = 1
            leftOffset = numRows - 2

            while leftOffset > 0:
                transposedZigzag.append(list(" " * leftOffset + s[index] + " " * rightOffset))
                horizontalLetters[numRows - rightOffset - 1].append(s[index])

                leftOffset -= 1
                rightOffset += 1
                index += 1
                if index >= len(s):
                    break
        
        for index, row in enumerate(horizontalLetters):
            row = "".join(row)
            horizontalLetters[index] = row
        
        return "".join(horizontalLetters)