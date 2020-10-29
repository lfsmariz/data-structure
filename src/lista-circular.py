class CircularNode:
    def __init__(self, values, next=None):
        try:
            len(values)
        except TypeError:
            values = list(values)
        self.value = values[0]
        self.next = self if next is None else next
        if len(values) >= 2:
            self.extend(values[1:])

    def __getitem__(self, index):
        if index == 0:
            return self.value
        return self.next.__getitem__(index + (1 if index < 0 else -1))

    def __setitem__(self, index, value):
        if index == 0:
            self.value = value
            return
        return self.next.__setitem__(index + (1 if index < 0 else -1), value)

    def __iter__(self):
        node = self
        while True:
            yield node.value
            node = node.next
            if node is self:
                return

    def __len__(self):
       return sum(1 for _ in self)

    def append(self, value):
        self.next = CircularNode([value], next=self.next)

    def extend(self, values):
        for value in reversed(values):
            self.append(value)

    def __repr__(self):
        return f"<Circular>[{', '.join(repr(item) for item in self)}]"

b = [2,3,4]
c = b[1:]
print(c)
a = CircularNode([2,3,4])
print(a)
