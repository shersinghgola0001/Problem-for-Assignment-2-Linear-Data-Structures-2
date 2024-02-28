#Q10. Implement a queue using the stack data structure.

class QueueUsingStacks:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def _transfer_elements(self):
        while self.enqueue_stack:
            self.dequeue_stack.append(self.enqueue_stack.pop())

    def dequeue(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                raise IndexError("Queue is empty")
            self._transfer_elements()
        return self.dequeue_stack.pop()

    def is_empty(self):
        return not (self.enqueue_stack or self.dequeue_stack)

    def size(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)

queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())
