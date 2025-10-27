# use two pointers starting at each end because that gives you optimal width,
# and then you adjust smaller point for height vs width trade-off
# considers all potentially optimal pairs without needing to check every pair

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        firstContainerWall = 0
        secondContainerWall = n - 1
        currentLargestArea = min(height[firstContainerWall], height[secondContainerWall]) # initialized to area of the initial container

        while (firstContainerWall != secondContainerWall):
            current_area = calc_area(firstContainerWall, secondContainerWall, height)
            if current_area > currentLargestArea:
                currentLargestArea = current_area
            
            if height[firstContainerWall] < height[secondContainerWall]:
                firstContainerWall += 1
            else:
                secondContainerWall -= 1

        return currentLargestArea

def calc_area(left, right, heights):
    return (right - left) * min(heights[left], heights[right])