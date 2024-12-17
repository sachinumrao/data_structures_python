class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# head_node -> next node -> next node

class LinkedList:
    def __init__(self):
        self.head : Node = None

    def __repr_(self):
        pass

    def __len__(self):
        n = 0
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            n += 1

        return n

    def __contains__(self):
        pass

    def append(self, val):
        '''add value at the end of linked list'''
        node = Node(val)
        if self.head is None:
            self.head = node

        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node


    def prepend(self, val):
        '''add value at beginning of linked lsit'''
        pass

    def insert(self, index, val):
        pass

    def delete(self, val):
        pass

    def pop(self):
        pass

    def popleft(self):
        pass


if __name__ == "__main__":
    # create linked list
    ll = LinkedList()

    # add items
    ll.append(5)
    ll.append(10)
    ll.append(20)
    ll.append(30)

    # print
    print(ll)
    print(len(ll))

    # delete elements
