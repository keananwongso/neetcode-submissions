class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.stack_min:
            self.stack_min.append(val)
        elif self.stack_min[-1] > val:
            self.stack_min.append(val)
        else:
            self.stack_min.append(self.stack_min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]

    # T: O(1)
    # S: O(n)