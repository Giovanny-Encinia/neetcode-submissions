class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:
            return None

        result = self.queue.pop()
        return result
    
    def top(self) -> int:
        return self.queue[-1] if self.queue else None    

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()