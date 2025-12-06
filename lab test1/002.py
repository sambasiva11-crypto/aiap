class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek into an empty queue.")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Test the Queue class
q = Queue()

# Scenario 1: Enqueue elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue after enqueues:", q.items)  # [10, 20, 30]

# Scenario 2: Peek at the front element
print("Peek:", q.peek())  # 10

# Scenario 3: Dequeue operations
print("Dequeue:", q.dequeue())  # 10
print("Queue after one dequeue:", q.items)  # [20, 30]

print("Dequeue:", q.dequeue())  # 20
print("Dequeue:", q.dequeue())  # 30

# Scenario 4: Edge cases - operations on an empty queue
try:
    q.dequeue()
except IndexError as e:
    print("Caught error on dequeue:", e)  # Proper error message

try:
    q.peek()
except IndexError as e:
    print("Caught error on peek:", e)  # Proper error message
