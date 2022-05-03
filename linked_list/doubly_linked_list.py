class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None

    def insert_at_beginning(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            self.tail=self.head
            return
        
        node = Node(data,self.head,None)
        self.head.prev = node
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            self.tail=self.head
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next =Node(data,None,itr)
        self.tail=itr.next
    
    def insert_at(self,index,data):
        if index <0 or index > self.get_length():
            raise Exception("Index out of bounds")
        if index == 0:
            self.insert_at_beginning(data)
            return
        elif index == self.get_length():
            self.insert_at_end(data)

        itr = self.head
        count =0
        while itr:
            if count == index-1:
                node = Node(data,itr.next,itr)
                itr.next.prev =node
                itr.next = node
                return
            count+=1
            itr=itr.next
    
    def remove_at(self,index):
        if index <0 or index >= self.get_length():
            raise Exception("Index out of bounds")
        
        if index ==0:
            if not self.head.next:
                self.head = None
                self.tail=None
                return
                
            else:
                self.head.next.prev=None
                self.head=self.head.next
                return
        elif index == self.get_length()-1:
            self.tail=self.tail.prev
            self.tail.next =None
        
        itr = self.head
        count=0
        while itr.next:
            if count == index:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
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

    def print_list_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        while itr:
            print(str(itr.data)+"-->",end='')
            itr = itr.next
        print("None")
    
    def print_list_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr=self.tail
        while itr:
            print(str(itr.data)+"-->",end='')
            itr = itr.prev
        print("None")

    def print_list_doubly(self):
        itr = self.head
        while itr:
            print(f"id={itr} data={itr.data} next={itr.next} prev={itr.prev}")
            itr = itr.next

    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        count=0
        while itr:
            if itr.data == data_after:
                self.insert_at(count+1,data_to_insert)
                return
            itr = itr.next
            count+=1
    
    def remove_by_value(self,data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
                return
            count+=1
            itr = itr.next

l1 = DoublyLinkedList()
l1.insert_at_beginning(7)
l1.insert_at_end(8)
l1.insert_at_end(9)
l1.insert_at(1,485)
l1.remove_at(0)
l1.insert_after_value(485,99)
l1.remove_at(3)
l1.print_list_doubly()
l1.print_list_forward()
l1.print_list_backward()