class MinStack:

    def __init__(self):
        self.stack_min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack_min) == 0:
            self.stack_min.append(val)
        else:
            if self.stack_min[-1] >= val:
                self.stack_min.append(val)

    def pop(self) -> None:
        result = self.stack.pop()

        if self.stack_min[-1] == result:
            self.stack_min.pop()
        
        return result

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack_min[-1]
        
