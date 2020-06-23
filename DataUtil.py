class Tree:
    def __init__(self):
        self.head = None
        self.data = -1
    def __init__(self, head):
        self.head = head
        self.data = -1
    def set(self, data):
        if data < 0:
            return None
        self.data = data