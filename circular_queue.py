# Q3 CircularQueue

# class declaration

class CircularQueue:

    def __init__(self, max_size):
        self.count = 0
        self.head = -1
        self.tail = -1
        self.max_size = max_size
        self.queue = [None] * max_size

    def enqueue(self, item):
        if self.count == self.max_size:
            print("cannot add, queue is full")
        elif self.head == -1:  # item being added, head and tail now take position in the queue
            self.head = 0
            self.tail = 0
            self.count += 1
            self.queue[self.tail] = item
        else:  # adding item to queue, tail gets added
            self.tail = (self.tail + 1) % self.max_size  # modulo to wrap back at beginning of queue if out of bounds
            self.queue[self.tail] = item
            self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("cannot remove, queue is empty")
        elif self.head == self.tail:  # removing final item in queue, reset head and tail
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:  # removing first in queue, second in queue now becomes first
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.max_size  # modulo to wrap back at beginning of queue if out of bounds
            self.count -= 1
            return temp

    def print_queue(self):
        if self.count == 0:
            print("queue is empty")
        elif self.tail >= self.head:  # tail has not wrapped around queue
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], "<-",
                      end=" ")  # print items and end with arrow pointing to item ahead in the queue
            print()  # newline separator
        else:  # tail has wrapped around queue
            for i in range(self.head, self.max_size):
                print(self.queue[i], "<-", end=" ")  # print items from head to end of list
            for i in range(0, self.tail + 1):
                print(self.queue[i], "<-", end=" ")  # print items from beginning of list to tail
            print()
