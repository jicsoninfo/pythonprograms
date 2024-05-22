class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self) -> None:
        self.root =None
        # self.incr_count = 0
    def height(self, node):
        if node is None:
            return 0
        return node.height
    
    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    
    def insert(self, node, key):
        # self.incr_count = self.incr_count+1;
        # print(node)
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)
        
        # Left Left Case
        if balance > 1 and key < node.left.key:
            print('left left case')
            return self.rotate_right(node)
        #Right Right Case
        if balance < -1 and key > node.right.key:
            print('right right case')
            print(balance)
            print(key)
            print(node.right.key)
            return self.rotate_left(node)
        #Left Right Case
        if balance > 1 and key > node.left.key:
            print('left right case')
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Right Left Case
        if balance < -1 and key < node.right.key:
            print('right left case')
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        # return balance
        print(node.height)
        # print(self.incr_count)
        print(balance)
        return node
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key)
            self.inorder_traversal(root.right)
        
    


avl_tree = AVLTree()
avl_tree.root = avl_tree.insert(avl_tree.root, 10)
avl_tree.root = avl_tree.insert(avl_tree.root, 20)
# avl_tree.root = avl_tree.insert(avl_tree.root, 15)
avl_tree.root = avl_tree.insert(avl_tree.root, 30)
# avl_tree.root = avl_tree.insert(avl_tree.root, 40)
# avl_tree.root = avl_tree.insert(avl_tree.root, 50)
# avl_tree.root = avl_tree.insert(avl_tree.root, 60)
# avl_tree.root = avl_tree.insert(avl_tree.root, 70)
# avl_tree.root = avl_tree.insert(avl_tree.root, 80)
# avl_tree.root = avl_tree.insert(avl_tree.root, 90)
# avl_tree.root = avl_tree.insert(avl_tree.root, 25)

avl_tree.inorder_traversal(avl_tree.root)

# print(avl_tree.root)        
        
