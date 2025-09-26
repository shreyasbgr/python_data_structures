class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        temp = self.head
        str_text =""
        while temp:
            str_text+=f"{temp.value} -> "
            temp = temp.next
        str_text+="NULL"
        return str_text
    
my_linked_list = LinkedList(4) 
print(my_linked_list)
