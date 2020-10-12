class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.tmp_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.tmp_stack:
            self.tmp_stack.append(x)
        elif x < self.tmp_stack[-1] and self.tmp_stack:
            self.tmp_stack.append(x)
        else:
            self.tmp_stack.append(self.tmp_stack[-1])
        return

    def pop(self) -> None:
        self.stack.pop()
        self.tmp_stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.tmp_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
