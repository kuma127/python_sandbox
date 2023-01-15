class BinaryTree:
    def __init__(self, value: int) -> None:
        self.key = value
        self.left_child: BinaryTree = None
        self.right_child: BinaryTree = None
    
    
    def insert_left(self, value: int) -> None:
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree
    

    def insert_right(self, value: int) -> None:
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree


    def breadth_firtst_search(self, n) -> bool:
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return False
    

    def invert(self) -> None:
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            current = next
            next = []
    

    def has_leaf_nodes(self) -> bool:
        if self.left_child or self.right_child:
            return True
        else:
            return False
    
    def preorder(self):
        preorder(self)
       

def preorder(tree: BinaryTree):
    if tree:
        # print(str(tree.key) + ' ' + str(tree.has_leaf_nodes()))
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)


## challenge
def preorder_invert(tree: BinaryTree):
    if tree:
        tmp = tree.left_child
        tree.left_child = tree.right_child
        tree.right_child = tmp
        preorder_invert(tree.left_child)
        preorder_invert(tree.right_child)


def postorder(tree: BinaryTree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)
    

def inorder(tree: BinaryTree):
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)


def main():
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.left_child.insert_left(4)
    tree.right_child.insert_left(5)
    tree.right_child.insert_right(6)
    tree.right_child.left_child.insert_left(7)
    tree.right_child.left_child.insert_right(8)
    # tree.invert()
    preorder_invert(tree)
    preorder(tree)


if __name__ == "__main__":
    main()
