# simplest case: i == h, k = max(piles)
# i == h + 1, k = second largest pile
# k is monotonic --> binary search!! (k can range from 1 to max(piles))

# if mid is a valid k and (mid - 1) is not a valid k, then this is the best solution, return mid
# if (mid - 1) is a valid k, then search left
# if mid is not a valid k, then search right

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def check_valid_k(k):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(float(pile) / k)
            
            return total_hours <= h
        
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if mid == 1:
                return 1 if check_valid_k(1) else 2

            if check_valid_k(mid) and not check_valid_k(mid - 1):
                return mid
            elif check_valid_k(mid) and check_valid_k(mid - 1):
                right = mid - 1
            else:
                left = mid + 1