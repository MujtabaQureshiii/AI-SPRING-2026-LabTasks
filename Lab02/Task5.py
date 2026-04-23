class CustomList:
    def __init__(self, size):
        self.arr = [None] * size
        self.count = 0
        self.size = size

    def insert(self, value):
        if self.count < self.size:
            self.arr[self.count] = value
            self.count += 1
        else:
            print("Custom List is Full")

    def delete(self, value):
        for i in range(self.count):
            if self.arr[i] == value:
                for j in range(i, self.count - 1):
                    self.arr[j] = self.arr[j + 1]
                self.arr[self.count - 1] = None
                self.count -= 1
                return
        print("Value Not Found in Custom List")

    def search(self, value):
        for i in range(self.count):
            if self.arr[i] == value:
                print(f"Value {value} found at index {i} in Custom List")
                return
        print(f"Value {value} not found in Custom List")

    def display(self):
        print("Custom List Elements:")
        if self.count == 0:
            print("  List is empty")
        else:
            for i in range(self.count):
                print(f"  Index {i}: {self.arr[i]}")


class Stack:
    def __init__(self, size):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def insert(self, value):   
        if self.top < self.size - 1:
            self.top += 1
            self.stack[self.top] = value
        else:
            print("Stack Overflow")

    def delete(self):          
        if self.top >= 0:
            self.stack[self.top] = None
            self.top -= 1
        else:
            print("Stack Underflow")

    def search(self, value):
        for i in range(self.top + 1):
            if self.stack[i] == value:
                print(f"Value {value} found in Stack")
                return
        print(f"Value {value} not found in Stack")

    def display(self):
        print("Stack Elements (Bottom → Top):")
        if self.top == -1:
            print("  Stack is empty")
        else:
            for i in range(self.top + 1):
                print(f"  Position {i}: {self.stack[i]}")


class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.size = size

    def insert(self, value):  
        if self.rear < self.size - 1:
            self.rear += 1
            self.queue[self.rear] = value
        else:
            print("Queue is Full")

    def delete(self):          
        if self.front <= self.rear:
            self.queue[self.front] = None
            self.front += 1
        else:
            print("Queue is Empty")

    def search(self, value):
        for i in range(self.front, self.rear + 1):
            if self.queue[i] == value:
                print(f"Value {value} found in Queue")
                return
        print(f"Value {value} not found in Queue")

    def display(self):
        print("Queue Elements (Front → Rear):")
        if self.front > self.rear:
            print("  Queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(f"  Position {i}: {self.queue[i]}")


# -------- Driver Code --------
cl = CustomList(5)
cl.insert(10)
cl.insert(20)
cl.insert(30)
cl.display()
cl.search(20)
cl.delete(20)
cl.display()

print()

s = Stack(5)
s.insert(5)
s.insert(10)
s.insert(15)
s.display()
s.delete()
s.display()

print()

q = Queue(5)
q.insert(1)
q.insert(2)
q.insert(3)
q.display()
q.delete()
q.display()
