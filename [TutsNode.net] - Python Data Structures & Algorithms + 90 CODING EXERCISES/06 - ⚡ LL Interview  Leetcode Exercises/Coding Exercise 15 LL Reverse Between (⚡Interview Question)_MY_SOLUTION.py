class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def remove_duplicates(self):
        elements_set = set()
        if self.length<0:
            return False
        elif self.length<=1 and self.length>=0:
            return True
        elif self.length == 2:
            if self.head.value == self.head.next.value:
                self.head.next = None
                self.length = 1
                return True
            else:
                return True
        else:
            elements_set = {self.head.value}
            pre = self.head
            post = self.head.next
            while post is not None:
                if post.value not in elements_set:
                    elements_set.add(post.value)
                    post = post.next
                    pre=pre.next  
                else:
                    pre.next = post.next
                    post.next = None
                    post = pre.next

    def find_kth_from_end(self,k):
        if self.length<=k or k<0:
            return None
        else:
            ahead = behind = self.head
            for _ in range(k):
                ahead = ahead.next

            while ahead.next:
                ahead = ahead.next
                if behind.next is not None:
                    behind = behind.next
            return behind
    def reverse_between(self, m, n):
        if m<0 or m>=self.length or n<0 or n>=self.length:
            return None
        elif m>=n:
            return None
        pre_m = self.head
        for _ in range(m-1):
            pre_m = pre_m.next

        tempend = None
        cur = pre_m.next
        m_th = cur
        for _ in range(n-m):
            curnext = cur.next
            cur.next = tempend
            tempend=cur
            cur = curnext
        post_n = cur.next
        cur.next = tempend
        pre_m.next = cur
        m_th.next = post_n
        
        


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(8)
my_linked_list.append(9)
my_linked_list.append(1)
print("Before reversing list:")
my_linked_list.print_list()
print(my_linked_list.reverse_between(1,4))
print("After reversing list:")
my_linked_list.print_list()
