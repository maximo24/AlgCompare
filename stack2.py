class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None  # true if null, false otherwise

    def push(self, item):
        if self.is_empty():  # if empty push at head item only
            self.head = Node(item)
        else:  # new node becomes head and head becomes next
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():  # cant pop if empty
            return "empty"
        else:  # head node gets replaced by next node
            pop_node = self.head
            self.head = self.head.next
            return pop_node.item

    def top(self):
        return self.head.item

    def size(self):
        if self.is_empty():
            return 0
        curr_node = self.head  # start at head node
        count = 0
        while curr_node is not None:  # count through every node until the next node is null
            count = count + 1
            curr_node = curr_node.next
        return count

    def print_stack(self):
        curr_node = self.head
        if self.is_empty():
            print("Stack is empty")
        else:  # print every node in stack until next node is null
            while curr_node is not None:
                print(curr_node.item, "->",
                      end=" ")  # seperate nodes with "->" and end print with space instead of line
                curr_node = curr_node.next
            return
