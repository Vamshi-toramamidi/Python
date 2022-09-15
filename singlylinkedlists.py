class node:
    def __init__(self,data=None):  # self keyword allows one to access instances and attributes of one's class
        self.data = data # stores the data 
        self.next = None # initially the next node is none 


class linked_list:
    def __init__(self):
        self.head = node() # it does not hold any value, We can't access it, it just holds the pointer to 1st node

    def append(self,data): # adds data to end of the list
        new_node = node(data) # we'll take the data from user and store it in new node
        cur = self.head 
        while cur.next != None: # iterates till we reach the end of the list ; We will know it as the end of list when next = None
            cur = cur.next 
                            # as soon as it knows that this end of list, it terminates
        cur.next = new_node # initializes the current node's next(pointer) to new node

    def erase(self,index):
        if index>=self.length():
            print("Out of Range")
            return None
        cur_index = 0  # Counter Variable
        cur_node = self.head 
        while True:
            last_node = cur_node 
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1
 
    def length(self):
        cur = self.head # We'll start from the head
        list_length = 0 # holds the length of the list
        while cur.next != None: # loop
            list_length += 1 # incrementing 
            cur = cur.next # traversing
        return list_length # returns the length of the list
    
    def display(self):
        elems = []  # We'll store the elements in this list (for our understanding)
        cur = self.head
        while cur.next != None:
            cur = cur.next # Pointing to the 1st node as head node does not contain any data
            elems.append(cur.data) # appending the data to list 
        print(elems)
    
    def get(self, index):
        if index >=self.length(): # If index is greater then we can't extract data
            print("OUT OF RANGE")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index +=1



# Drivers code
my_list = linked_list()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.length()
print(my_list.get(4))

my_list.display()


        
