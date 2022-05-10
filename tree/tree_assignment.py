class TreeNode:
    def __init__(self, name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,type):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if type == "both":
            print(prefix + self.name+' '+"({})".format(self.designation))
        elif type == "name":
            print(prefix + self.name)
        elif type == "designation":
            print(prefix + self.designation)
        if self.children:
            for child in self.children:
                child.print_tree(type)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    root = TreeNode("Nilupul","CEO")
    chinmay = TreeNode("Chinmay","CTO")
    gels = TreeNode("Gels","HR Head")

    vishwa = TreeNode("Vishwa","Infrastructure Head")
    vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    vishwa.add_child(TreeNode("Abhijit", "App Manager"))
    aamir = TreeNode("Aamir", "Application Head")
    chinmay.add_child(vishwa)
    chinmay.add_child(aamir)

    gels.add_child(TreeNode("Peter", "Recruitment Manager"))
    gels.add_child(TreeNode("Waqas", "Policy Manager"))


    root.add_child(chinmay)
    root.add_child(gels)
    return root

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy