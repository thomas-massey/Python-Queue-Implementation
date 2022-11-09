# This is a simple python implemetation of a Queue

class Queue:
    def __init__(self):
        self.queue = []
        self.queue_length = 0
        self.order = []
        self.empty = []
        self.find_iteration = 0

    def enqueue(self, data):
        if self.queue == []:
            self.queue.append(data)
            self.queue_length += 1
            self.order.append(self.find_iteration)
        elif self.empty != []:
            self.queue[self.empty[0]] = data
            self.order[self.empty[0]] = self.find_iteration + self.queue_length
            self.queue_length += 1
            self.empty.pop(0)
        else:
            self.queue.append(data)
            self.order.append(self.find_iteration + self.queue_length)
            self.queue_length += 1

    def dequeue(self):
        if self.queue_length == 0:
            return None
        else:
            cache_value = self.queue[self.order.index(self.find_iteration)]
            self.queue_length -= 1
            self.find_iteration += 1
            self.empty.append(self.order.index(self.find_iteration))
            return cache_value

    def __str__(self):
        return_array = []
        return_array_length = 0
        for i in self.order:
            if return_array_length > self.queue_length:
                return str(return_array)
            if i >= self.find_iteration:
                return_array.append(self.queue[i])
                return_array_length += 1
        return str(return_array)

    def is_empty(self):
        if self.queue_length == 0:
            return True
        else:
            return False

    def size(self):
        return self.queue_length

    def peek(self):
        if self.queue_length == 0:
            return None
        else:
            return self.queue[self.order.index(self.find_iteration)]

def main():
    print("Welcome to the Queue implementation")
    queue = Queue()
    running = True
    while running:
        print("""
    1. Enqueue
    2. Dequeue
    3. Print Queue
    4. Check if Queue is empty
    5. Check size of Queue
    6. Peek at the first element
    7. Other (Debugging)
    8. Exit
    """)
        choice = str(input("Enter your choice: "))
        if choice == "1":
            data = input("Enter the data to be enqueued: ")
            queue.enqueue(data)
        elif choice == "2":
            print(queue.dequeue())
        elif choice == "3":
            print(queue)
        elif choice == "4":
            print(queue.is_empty())
        elif choice == "5":
            print(queue.size())
        elif choice == "6":
            print(queue.peek())
        elif choice == "7":
            running_debug_mode = True
            while running_debug_mode:
                print("""
    1. Print Queue
    2. Print Queue Length
    3. Print Order
    4. Print Empty
    5. Print Find Iteration
    6. Print All
                """)
                choice = str(input("Enter your choice: "))
                if choice == "1":
                    print(queue.queue)
                elif choice == "2":
                    print(queue.queue_length)
                elif choice == "3":
                    print(queue.order)
                elif choice == "4":
                    print(queue.empty)
                elif choice == "5":
                    print(queue.find_iteration)
                elif choice == "6":
                    print(f"Queue = {queue.queue}")
                    print(f"Queue Length = {queue.queue_length}")
                    print(f"Order = {queue.order}")
                    print(f"Empty Location Array = {queue.empty}")
                    print(f"Search Iteration = {queue.find_iteration}")
                else:
                    running_debug_mode = False
        elif choice == "8":
            running = False
        else:
            print("Invalid Choice")

main()