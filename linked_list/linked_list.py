class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next =Node(data,None)
    
    def insert_at(self,index,data):
        if index <0 or index > self.get_length():
            raise Exception("Index out of bounds")
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        itr = self.head
        count =0
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                return
            count+=1
            itr=itr.next
    
    def remove_at(self,index):
        if index <0 or index > self.get_length():
            raise Exception("Index out of bounds")
        itr = self.head
        count=0
        while itr.next:
            if count == index-1:
                itr.next = itr.next.next
                return
            itr=itr.next
            count+=1

    def insert_values(self,values):
        self.head=None
        for value in values:
            self.insert_at_end(value)
    
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return count

    def print_list(self):
        itr = self.head
        while itr:
            print(str(itr.data)+"-->",end='')
            itr = itr.next
        print("None")

l1 = LinkedList()
l1.insert_at_beginning(67)
l1.insert_at_beginning(77)
l1.insert_at_end(80)
l1.insert_at_end(98)
l1.insert_at_beginning(1)
print("List earlier:")
l1.print_list()
l1.insert_at(3,485)
l1.remove_at(4)
print("List after:")
l1.print_list()
l1.insert_values([7,5,4,9,10,11])
print("List after inserting values:")
l1.print_list()
