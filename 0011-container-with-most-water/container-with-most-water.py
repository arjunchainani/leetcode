# maximize area -> base -- second i value minus first i value
# height -- lowest height between the two values
# BCR: O(n)


# pass through the array
# two pointers --> one of them corresponds to the left wall of the container and the second corresponds to the right wall
#      init at (0, 1)
#      variable to store current largest area --> return this at the end
#      while ptrs dont get to (n-1, n)
#            increment ptr with lower height and check if you have a new highest area
#                if not, keep incrementing until you hit the end of the array and checking
#                if you do, update the current largest area var, and then repeat the inner loop

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