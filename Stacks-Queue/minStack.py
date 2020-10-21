class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.min.append(x)
            self.stack.append(x)
            return
        if x <= self.min[-1]:
            self.min.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
