class MinStack(object):

    def __init__(self):
        self.height = 0
        self.values = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.values.append(val)
        self.height += 1
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        popped = self.values.pop(self.height - 1)
        self.height -= 1
        if self.min_stack[-1] == popped:
            self.min_stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.values[self.height - 1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) != 0:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()