class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.stack and not self.min_stack:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            min_val = min(val, self.min_stack[-1])
            self.stack.append(val)
            self.min_stack.append(min_val)
    
    def pop(self) -> None:
        if not self.stack and not self.min_stack:
            return None
        else:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if not self.stack and not self.min_stack:
            return -1
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return -1
        else:
            return self.min_stack[-1]


min_stack = MinStack()

min_stack.push(5)
min_stack.push(3)
min_stack.push(8)
min_stack.push(2)

print(min_stack.getMin())  # 2

min_stack.pop()
print(min_stack.getMin())  # 3

print(min_stack.top())     # 8