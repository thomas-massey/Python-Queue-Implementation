# This is a simple python implemetation of a Queue

class Queue:
    def __init__(self):
        self.queue = []
        self.queue_length = 0
        self.order = []
        self.empty = []
        self.find_iteration = 0

    def enqueue(self, data):
        if self.empty == []:
            self.empty.append(data)
            self.queue.append(data)
            self.order.append(len(self.queue) - 1)
            self.queue_length += 1
        else:
            self.queue[self.empty[0]] = data
            self.order.append(self.empty[0])
            self.empty.pop(0)
            self.queue_length += 1

    def dequeue(self):
        if self.queue_length == 0:
            return None
        else:
            self.queue[self.order[self.find_iteration]] = None
            self.find_iteration += 1
            self.queue_length -= 1
            self.empty.append(self.order[self.find_iteration])
            return self.queue[self.order[self.find_iteration - 1]]

    def is_empty(self):
        if self.queue_length == 0:
            return True
        else:
            return False

    def peek():
        pass

    def size():
        pass