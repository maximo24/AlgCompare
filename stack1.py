class Stack:

    def __init__(self):
        self.items = []  # initialize list

    def is_empty(self):
        return self.items == []  # True if empty, False otherwise

    def push(self, item):
        self.items.append(item)  # add item to the stack

    def pop(self):
        return self.items.pop()  # removes item at top of stack

    def top(self):
        return self.items[len(self.items)-1]  # returns item at top of stack

    def size(self):
        return len(self.items)  # return the number of items in the stack
