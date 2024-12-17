class Node:
    def __init__(self, data):
        """Initialize a Node with data and next pointer."""
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self._size = 0

    def is_empty(self):
        """Return True if the list is empty, False otherwise."""
        return self.head is None

    def size(self):
        """Return the number of nodes in the list."""
        return self._size

    def insert_front(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def insert_at(self, data, position):
        """Insert a new node at the specified position."""
        if position < 0 or position > self._size:
            raise IndexError("Invalid position")

        if position == 0:
            self.insert_front(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def delete_front(self):
        """Remove and return the first element of the list."""
        if self.head is None:
            raise IndexError("Cannot delete from empty list")

        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def delete_end(self):
        """Remove and return the last element of the list."""
        if self.head is None:
            raise IndexError("Cannot delete from empty list")

        if self.head.next is None:
            data = self.head.data
            self.head = None
            self._size -= 1
            return data

        current = self.head
        while current.next.next:
            current = current.next

        data = current.next.data
        current.next = None
        self._size -= 1
        return data

    def delete_at(self, position):
        """Remove and return the element at the specified position."""
        if position < 0 or position >= self._size:
            raise IndexError("Invalid position")

        if position == 0:
            return self.delete_front()

        current = self.head
        for _ in range(position - 1):
            current = current.next

        data = current.next.data
        current.next = current.next.next
        self._size -= 1
        return data

    def find(self, data):
        """Return the position of the first occurrence of data, or -1 if not found."""
        current = self.head
        position = 0

        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1

        return -1

    def get_at(self, position):
        """Return the data at the specified position without removing it."""
        if position < 0 or position >= self._size:
            raise IndexError("Invalid position")

        current = self.head
        for _ in range(position):
            current = current.next

        return current.data

    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def to_list(self):
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        """Return a string representation of the linked list."""
        return " -> ".join(str(item) for item in self.to_list())


if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()

    # Insert elements
    ll.insert_end(1)  # 1
    ll.insert_end(2)  # 1 -> 2
    ll.insert_front(0)  # 0 -> 1 -> 2
    ll.insert_at(1.5, 2)  # 0 -> 1 -> 1.5 -> 2

    print(ll)  # Output: 0 -> 1 -> 1.5 -> 2

    # Access elements
    print(ll.get_at(2))  # Output: 1.5
    print(ll.find(1.5))  # Output: 2 (position)

    # Delete elements
    ll.delete_front()  # 1 -> 1.5 -> 2
    ll.delete_end()  # 1 -> 1.5
    ll.delete_at(1)  # 1

    # Other operations
    print(ll.size())  # Output: 1
    ll.reverse()  # Reverses the list in-place
    print(ll.to_list())  # Converts to Python list: [1]
