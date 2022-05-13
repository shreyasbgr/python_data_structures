class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        
        else:
            return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        
        else:
            return self.data
    
    def calculate_sum(self):
        sum = 0
        if self.left:
            sum+=self.left.calculate_sum()

        sum+=self.data

        if self.right:
            sum+=self.right.calculate_sum()
        
        return sum
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements+=self.left.post_order_traversal()
        
        if self.right:
            elements+=self.right.post_order_traversal()
        
        elements.append(self.data)
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements+=self.left.post_order_traversal()
        
        if self.right:
            elements+=self.right.post_order_traversal()
        
        return elements

    def delete(self,node):
        if node > self.data:
            if self.right:
                self.right = self.right.delete(node)
            return self

        elif node < self.data:
            if self.left:
                self.left = self.left.delete(node)
            return self
        else:
            if self.left:
                max_left = self.left.find_max()
                self.data = max_left
                self.left = self.left.delete(max_left)
                return self
            elif self.right:
                min_right = self.right.find_min()
                self.data = min_right
                self.right = self.right.delete(min_right)
                return self
            else:
                return None

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("Minimum element is ",numbers_tree.find_min())
    print("Maximum element is ",numbers_tree.find_max())
    print("Sum of elements is ",numbers_tree.calculate_sum())
    print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())

    numbers_tree.delete(17)
    print(numbers_tree.in_order_traversal())
