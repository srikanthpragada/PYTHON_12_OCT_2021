import json


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


c1 = Circle(10, 20, 15)
s = json.dumps(c1.__dict__)  # Convert object to JSON string
print(s)

d = json.loads(s)
print(d)