class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(item)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Can't pop from empty queue")
        return self.s1.pop()


# challenge: replace Queue to O(1)
class Queue_01:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        if not self.s1:
            self.s1.append(item)
            return
        self.s2.append(item)
        self.s1 = self.s2 + self.s1
        self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Can't pop from empty queue")
        return self.s1.pop()


def main():
    queue = Queue_01()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(2)
    for i in range(4):
        print(queue.dequeue())


if __name__ == "__main__":
    main()
