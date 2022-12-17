class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def __str__(self) -> str:
        data_list = []
        node = self.head
        while node is not None:
            data_list.append(str(node.data))
            node = node.next
        return "\n".join(data_list)

    def search(self, target) -> bool:
        current = self.head
        while current:
            if current.data == target:
                return True
            else:
                current = current.next
        return False

    def remove(self, target) -> None:
        if self.head.data == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

    def reverse_list(self) -> None:
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def detect_cycle(self) -> bool:
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except AttributeError:
                return False


def main():
    list = LinkedList()
    # challenge
    for num in range(1, 101):
        list.append(num)
    print(list.head.next.data)


if __name__ == "__main__":
    main()
