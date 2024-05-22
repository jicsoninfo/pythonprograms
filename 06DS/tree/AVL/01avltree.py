class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

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
            return self.rotate_right(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def delete(self, root, key):
        if root is None:
            return root
        
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        
        if root is None:
            return root
        
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left Left Case
        if balance > 1 and self.balance(root.left) >= 0:
            return self.rotate_right(root)

        # Left Right Case
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and self.balance(root.right) <= 0:
            return self.rotate_left(root)

        # Right Left Case
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if root.key < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

# Usage example:
avl_tree = AVLTree()
avl_tree.root = avl_tree.insert(avl_tree.root, 10)
avl_tree.root = avl_tree.insert(avl_tree.root, 20)
avl_tree.root = avl_tree.insert(avl_tree.root, 30)
avl_tree.root = avl_tree.insert(avl_tree.root, 40)
avl_tree.root = avl_tree.insert(avl_tree.root, 50)
avl_tree.root = avl_tree.insert(avl_tree.root, 25)

print("Inorder traversal of the constructed AVL tree is:")
avl_tree.inorder_traversal(avl_tree.root)

avl_tree.root = avl_tree.delete(avl_tree.root, 20)

print("\nInorder traversal after deletion of 20:")
avl_tree.inorder_traversal(avl_tree.root)

print("\nSearch for key 30:")
result = avl_tree.search(avl_tree.root, 30)
if result:
    print("Key found!")
else:
    print("Key not found!")
