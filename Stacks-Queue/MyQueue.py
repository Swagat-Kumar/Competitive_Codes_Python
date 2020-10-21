class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.oldest = []
        self.newest = []

    def copier(self):
        if len(self.oldest) == 0:
            while len(self.newest) != 0:
                self.oldest.append(self.newest.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.newest.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.copier()
        return self.oldest.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.copier()
        return self.oldest[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.oldest)+len(self.newest) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
