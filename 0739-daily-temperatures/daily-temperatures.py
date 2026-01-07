# use a monotonically decreasing stack, whenever you pop an index off, update that answer[index] with the difference between the current index (i) and that popped index
# make sure that stack stores the indices of the days and not the actual temp, but compare using the actual temp
# at the end of the loop, whichever indices are still on the stack should have their answer[i] set to 0 (since no warmer temp was ever found)

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev

            stack.append(i)

        return answer