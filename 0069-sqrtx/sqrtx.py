class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        l = 0
        r = x
        return findSqrt(l, r, x)

        
def findSqrt(l, r, x):
    m = (l + r) // 2

    if l > r:
        return r

    if m * m == x:
        return m
    elif m * m > x:
        return findSqrt(l, m - 1, x)
    elif m * m < x:
        return findSqrt(m + 1, r, x)
