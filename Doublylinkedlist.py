class node:
    def __init__(self, data=None):  # Node class to hold data and pointers to previous and next nodes
        self.data = data            # stores the data
        self.next = None            # pointer to the next node
        self.prev = None            # pointer to the previous node


class doubly_linked_list:
    def __init__(self):
        self.head = node()  # Dummy head node, does not hold data but points to the first actual node

    def append(self, data):  # Adds a new node at the end
        new_node = node(data)
        cur = self.head
        while cur.next != None:  # Traverse till end
            cur = cur.next
        cur.next = new_node      # Link last node's next to new node
        new_node.prev = cur      # Link new node's prev to last node

    def length(self):  # Returns length of the list
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display_forward(self):  # Displays list from head to tail
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print("Forward:", elems)

    def display_backward(self):  # Displays list from tail to head
        cur = self.head
        while cur.next != None:  # Go to the last node
            cur = cur.next
        elems = []
        while cur.prev != None:  # Traverse backward
            elems.append(cur.data)
            cur = cur.prev
        print("Backward:", elems)

    def get(self, index):  # Returns data at given index
        if index >= self.length():
            print("OUT OF RANGE")
            return None
        cur_index = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_index == index:
                return cur.data
            cur_index += 1

    def erase(self, index):  # Removes node at the given index
        if index >= self.length():
            print("Out of Range")
            return
        cur_index = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur_index == index:
                prev_node = cur.prev
                next_node = cur.next
                if next_node != None:
                    next_node.prev = prev_node
                prev_node.next = next_node
                return
            cur_index += 1


# Driver Code
my_dll = doubly_linked_list()

my_dll.append(10)
my_dll.append(20)
my_dll.append(30)
my_dll.append(40)
my_dll.append(50)

print("Length:", my_dll.length())
print("Element at index 2:", my_dll.get(2))

my_dll.display_forward()
my_dll.display_backward()

my_dll.erase(2)
print("After erasing index 2:")
my_dll.display_forward()
my_dll.display_backward()
