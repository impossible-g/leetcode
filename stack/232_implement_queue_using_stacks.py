class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack_in and not self.stack_out:
            return True
        else:
            return False


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_3 = obj.peek()
param_2 = obj.pop()
param_1 = obj.pop()
param_4 = obj.empty()
print(param_3, param_2, param_1, param_4)
