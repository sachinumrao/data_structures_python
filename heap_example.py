class BinaryHeap:
    def __init__(self, is_min_heap=True):
        """Initialize an empty heap. By default creates a min heap."""
        self.heap = []
        self.is_min_heap = is_min_heap

    def parent(self, i):
        """Return the parent index of node at index i."""
        return (i - 1) // 2

    def left_child(self, i):
        """Return the left child index of node at index i."""
        return 2 * i + 1

    def right_child(self, i):
        """Return the right child index of node at index i."""
        return 2 * i + 2

    def swap(self, i, j):
        """Swap elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def compare(self, a, b):
        """Compare two elements based on heap type."""
        return a < b if self.is_min_heap else a > b

    def heapify_up(self, i):
        """Maintain heap property by floating up element at index i."""
        parent = self.parent(i)
        if i > 0 and self.compare(self.heap[i], self.heap[parent]):
            self.swap(i, parent)
            self.heapify_up(parent)

    def heapify_down(self, i):
        """Maintain heap property by sinking down element at index i."""
        min_idx = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.compare(self.heap[left], self.heap[min_idx]):
            min_idx = left

        if right < len(self.heap) and self.compare(
            self.heap[right], self.heap[min_idx]
        ):
            min_idx = right

        if min_idx != i:
            self.swap(i, min_idx)
            self.heapify_down(min_idx)

    def insert(self, key):
        """Insert a new key into the heap."""
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def extract(self):
        """Remove and return the root element (min/max depending on heap type)."""
        if not self.heap:
            raise IndexError("Heap is empty")

        root = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self.heapify_down(0)

        return root

    def peek(self):
        """Return the root element without removing it."""
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def is_empty(self):
        """Return True if heap is empty, False otherwise."""
        return len(self.heap) == 0


if __name__ == "__main__":
    min_heap = BinaryHeap()

    # Insert some values
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(7)
    min_heap.insert(1)

    # Extract values (will come out in ascending order)
    while not min_heap.is_empty():
        print(min_heap.extract())  # Outputs: 1, 3, 5, 7

    # Create a max heap
    max_heap = BinaryHeap(is_min_heap=False)

    # Insert values
    max_heap.insert(5)
    max_heap.insert(3)
    max_heap.insert(7)
    max_heap.insert(1)

    # Extract values (will come out in descending order)
    while not max_heap.is_empty():
        print(max_heap.extract())
