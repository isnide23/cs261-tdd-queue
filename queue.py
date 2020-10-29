# Queue: A queue.
# Your implementation should pass the tests in test_queue.py.
# Ian Snyder

# Hint: pip3 install llist
# from llist import sllist

from llist import sllist

class Queue:

    def __init__(self):
        self.data = sllist()
        

    def enqueue(self, value):
        self.data.append(value)
        
        
    def dequeue(self):
        if self.data.size < 0:
            raise ValueError
        return self.data.popleft()

    def is_empty(self):
        if self.data.size == 0:
            return True
        elif self.data.size >= 0:
            return False

    
        

    



