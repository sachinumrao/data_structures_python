from ast import parse


class Heap:
    def __init__(self, arr):
        self._data = arr
        self.heapify()

    def heapify(self):
        # starting from last element, pick element -> find parent -> comapre and swap
        node_id = len(self._data) - 1

        # num: 0,5,6,1,2,2,3
        # idx: 0,1,2,3,4,5,6   => parent = (child-1)//2 , (5,6) -> 2, (1,2) -> 0, (3,4) -> 1

        while node_id > 0:
            parent_node_id = (node_id - 1) // 2
            if self._data[parent_node_id] > self._data[node_id]:
                tmp = self._data[node_id]
                self._data[node_id] = self._data[parent_node_id]
                self._data[parent_node_id] = tmp

            node_id -= 1

        pass

    def push(self, x):
        self._data.append(x)
        self.heapify()

    def pop(self):
        if self._data:
            item = self._data[0]
            self._data = self._data[1:]
            self.heapify()
            return item
        else:
            raise Exception("Tryinh to remove item from an empty heap...")

    def peek(self):
        if self._data:
            return self._data[0]
        else:
            raise Exception("Trying to lookup an item in empty heap...")

    def __len__(self):
        return len(self._data)


if __name__ == "__main__":
    arr = [10, 15, 24, 38, 32, 1, 40]
    hp = Heap(arr)

    while len(hp) > 0:
        item = hp.pop()
        print(item)
