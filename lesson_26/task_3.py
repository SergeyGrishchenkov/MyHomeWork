# Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

# Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue.
# Any other element must remain in the queue respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message
#


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def get_from_stack(self, e):
       try:
           return self.stack.pop(self.stack.index(e))
       except ValueError:
           print(f"Not such Value: {e} in Stack")
           return None

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def __repr__(self):
        return f'Now stack is : {self.stack}'
# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return True if len(self.queue) == 0 else False

    def get_from_queue(self, e):
        try:
            return self.queue.pop(self.queue.index(e))
        except ValueError:
            print(f"Not such Value: {e} in Queue")
            return None

    def __repr__(self):
        return f'Now queue is : {self.queue}'

if __name__ == '__main__':
    stack_test = Stack()
    for item in range(11):
        stack_test.push(item)
    print(stack_test)
    stack_test.get_from_stack(7)
    print(stack_test)
    stack_test.get_from_stack(71)
    print(stack_test)
    print("*"*20)
    q1 = Queue()
    print(f'Empty: {q1.is_empty()}')
    for item in range(5, 26, 2):
        q1.enqueue(item)
    print(q1)
    q1.get_from_queue(17)
    print(q1)
    q1.get_from_queue(18)
    print(q1)
