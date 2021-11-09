class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def isempty(self):
        return len(self.data) == 0

    @property
    def length(self):
        return len(self.data)

    def clear(self):
        self.data.clear()


s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.length)
print(s.peek())

