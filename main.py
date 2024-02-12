import k_comparison
import stack1
import stack2
import circular_queue

# Question 1
print("\nQUESTION 1 we test the smallest k value for when binary search is faster than linear search\n")
print("Test cases: n = 1000, n = 5000, n = 10000")
print(k_comparison.smallest_k(1000))
print(k_comparison.smallest_k(5000))
print(k_comparison.smallest_k(10000))

# Question 2
print("\nQUESTION 2: Implementing a stack\n")
print("\nARRAY BASED LIST:\n")

s1 = stack1.Stack()

print("is_empty()")
print(s1.is_empty())

print("push('a')")
print("push('b')")
print("push('c')")
print("push('d')")
s1.push('a')
s1.push('b')
s1.push('c')
s1.push('d')

print("stack:")
print(s1.items)

print('pop()')
print('pop()')
s1.pop()
s1.pop()

print("stack:")
print(s1.items)

print("top()")
print(s1.top())

print("size()")
print(s1.size())

print("\nLINKED LIST:\n")

s2 = stack2.Stack()

print("is_empty()")
print(s2.is_empty())

print("push('a')")
print("push('b')")
print("push('c')")
print("push('d')")
s2.push("a")
s2.push("b")
s2.push("c")
s2.push("d")

print("stack:")
s2.print_stack()

print("\npop()")
print("pop()")
s2.pop()
s2.pop()

print("stack:")
s2.print_stack()

print("\ntop()")
print(s2.top())

print("size()")
print(s2.size())

# Question 3
print("\nQUESTION 3: Circular Queue\n")

q = circular_queue.CircularQueue(5)

print("dequeue()")
q.dequeue()

print("enqueue('a')")
q.enqueue("a")
print("enqueue('b')")
q.enqueue("b")
print("enqueue('c')")
q.enqueue("c")
print("enqueue('d')")
q.enqueue("d")
print("enqueue('e')")
q.enqueue("e")

print("print_queue()")
q.print_queue()

print("dequeue()")
q.dequeue()

print("print_queue()")
q.print_queue()

print("dequeue")
q.dequeue()

print("enqueue('z')")
q.enqueue("z")

print("enqueue('f')")
q.enqueue("f")

print("print_queue()")
q.print_queue()

print("enqueue('g')")
q.enqueue("g")
