# use a monotonically decreasing stack, at the end of each iteration through a daily temp, whatever day indices are still on the stack should have their answer[i] incremented
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