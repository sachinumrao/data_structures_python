class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# add element at start
def add_begin(a, val):
    b = ListNode(val)
    b.next = a
    return b

# add element at end
def add_end(a, val):
    x = a
    while x.next is not None:
        x = x.next

    x.next = ListNode(val)
    return a

# add at specific index
def add_mid(a, val, ind):
    x = a
    counter = 0
    while counter < ind-1 :
        x = x.next
        if x is None:
            print("Trying to add at place out of bound...")
            return a
        counter += 1
    tmp = x.next
    b = ListNode(val)
    b.next = tmp
    x.next = b
    return a


def remove_from_head(a):
    return a.next

def remove_from_tail(a):
    x = a
    while x.next.next is not None:
        x = x.next

    x.next = None
    return a

def remove_from_mid(a, ind):
    x = a
    counter = 0
    while counter < ind-1:
        x = x.next
        if x is None:
            print("Trying to delete at a place out of bound...")
            return a
        counter += 1
    x.next = x.next.next
    return a
        
def find_length(a):
    counter = 0
    x = a
    while x is not None:
        x = x.next
        counter += 1

    return counter


a = ListNode(1)
a = add_begin(a, 0)
a = add_begin(a, -1)
a = add_begin(a, -2)

a = add_end(a,2)
a = add_end(a,3)

a = add_mid(a, 0, 2)
a = remove_from_mid(a, 2)
n = find_length(a)


print("Length of Linked List : ", n)
#a = remove_from_head(a)
#a = remove_from_tail(a)

# Traversing the list
x = a
while x is not None:
    print(x.val)
    x = x.next
