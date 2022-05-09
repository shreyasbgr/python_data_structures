from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

binary_nos = Queue()

def produce_binary_nos(n):
    binary_nos.enqueue("1")
    for i in range(n):
        print(binary_nos.front())
        binary_nos.enqueue(binary_nos.front() +"0")
        binary_nos.enqueue(binary_nos.front() +"1")

        binary_nos.dequeue()

if __name__ == '__main__':
    produce_binary_nos(10)