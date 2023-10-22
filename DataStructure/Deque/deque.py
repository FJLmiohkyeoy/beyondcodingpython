class Deque:
    def __init__(self):
        self.items = []

    def pushLeft(self, item):
        self.items.insert(0, item)

    def pushRight(self, item):
        self.items.append(item)

    def popLeft(self):
        self.items.pop(0)

    def popRight(self):
        self.items.pop()

    def getFront(self):
        return self.items[0]

    def getBack(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0
