#4. More Control Flow Tools
#4.1. if Statements 
# Perhaps the most well-known statement type is the if statement. For example:
x = int(input("Please enter an integer: ")) #Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
#More


'''<?php

class Node {
    public $data;
    public $left;
    public $right;
    public $height;

    public function __construct($data) {
        $this->data = $data;
        $this->left = null;
        $this->right = null;
        $this->height = 1;
    }
}

class AVLTree {
    private $root;

    public function __construct() {
        $this->root = null;
    }

    // Helper function to get height of the node
    private function height($node) {
        if ($node === null) return 0;
        return $node->height;
    }

    // Helper function to get balance factor of the node
    private function getBalance($node) {
        if ($node === null) return 0;
        return $this->height($node->left) - $this->height($node->right);
    }

    // Function to perform right rotation
    private function rightRotate($y) {
        $x = $y->left;
        $T2 = $x->right;

        $x->right = $y;
        $y->left = $T2;

        $y->height = max($this->height($y->left), $this->height($y->right)) + 1;
        $x->height = max($this->height($x->left), $this->height($x->right)) + 1;

        return $x;
    }

    // Function to perform left rotation
    private function leftRotate($x) {
        $y = $x->right;
        $T2 = $y->left;

        $y->left = $x;
        $x->right = $T2;

        $x->height = max($this->height($x->left), $this->height($x->right)) + 1;
        $y->height = max($this->height($y->left), $this->height($y->right)) + 1;

        return $y;
    }

    // Function to insert a node
    public function insert($root, $data) {
        if ($root === null) {
            return new Node($data);
        }

        if ($data < $root->data) {
            $root->left = $this->insert($root->left, $data);
        } elseif ($data > $root->data) {
            $root->right = $this->insert($root->right, $data);
        } else {
            // Duplicate data not allowed
            return $root;
        }

        $root->height = 1 + max($this->height($root->left), $this->height($root->right));

        $balance = $this->getBalance($root);

        // Left Left Case
        if ($balance > 1 && $data < $root->left->data) {
            return $this->rightRotate($root);
        }

        // Right Right Case
        if ($balance < -1 && $data > $root->right->data) {
            return $this->leftRotate($root);
        }

        // Left Right Case
        if ($balance > 1 && $data > $root->left->data) {
            $root->left = $this->leftRotate($root->left);
            return $this->rightRotate($root);
        }

        // Right Left Case
        if ($balance < -1 && $data < $root->right->data) {
            $root->right = $this->rightRotate($root->right);
            return $this->leftRotate($root);
        }

        return $root;
    }

    // Function to traverse the tree in inorder
    public function inorder($node) {
        if ($node !== null) {
            $this->inorder($node->left);
            echo $node->data . " ";
            $this->inorder($node->right);
        }
    }

    // Function to search for a node
    public function search($root, $data) {
        if ($root === null || $root->data === $data) {
            return $root;
        }

        if ($data < $root->data) {
            return $this->search($root->left, $data);
        }

        return $this->search($root->right, $data);
    }

    // Function to find the node with minimum value
    public function minValueNode($node) {
        $current = $node;

        while ($current->left !== null) {
            $current = $current->left;
        }

        return $current;
    }

    // Function to delete a node
    public function delete($root, $data) {
        if ($root === null) {
            return $root;
        }

        if ($data < $root->data) {
            $root->left = $this->delete($root->left, $data);
        } elseif ($data > $root->data) {
            $root->right = $this->delete($root->right, $data);
        } else {
            if ($root->left === null || $root->right === null) {
                $temp = ($root->left !== null) ? $root->left : $root->right;

                if ($temp === null) {
                    $temp = $root;
                    $root = null;
                } else {
                    $root = $temp;
                }
            } else {
                $temp = $this->minValueNode($root->right);
                $root->data = $temp->data;
                $root->right = $this->delete($root->right, $temp->data);
            }
        }

        if ($root === null) {
            return $root;
        }

        $root->height = 1 + max($this->height($root->left), $this->height($root->right));

        $balance = $this->getBalance($root);

        // Left Left Case
        if ($balance > 1 && $this->getBalance($root->left) >= 0) {
            return $this->rightRotate($root);
        }

        // Left Right Case
        if ($balance > 1 && $this->getBalance($root->left) < 0) {
            $root->left = $this->leftRotate($root->left);
            return $this->rightRotate($root);
        }

        // Right Right Case
        if ($balance < -1 && $this->getBalance($root->right) <= 0) {
            return $this->leftRotate($root);
        }

        // Right Left Case
        if ($balance < -1 && $this->getBalance($root->right) > 0) {
            $root->right = $this->rightRotate($root->right);
            return $this->leftRotate($root);
        }

        return $root;
    }
}

// Example usage:
$tree = new AVLTree();
$root = null;

$root = $tree->insert($root, 10);
$root = $tree->insert($root, 20);
$root = $tree->insert($root, 30);
$root = $tree->insert($root, 40);
$root = $tree->insert($root, 50);
$root = $tree->insert($root, 25);

echo "Inorder traversal of the constructed AVL tree is: \n";
$tree->inorder($root);

echo "\nSearching for 30: ";
$result = $tree->search($root, 30);
if ($result !== null) {
    echo "Found\n";
} else {
    echo "Not Found\n";

}

echo "Deleting 30...\n";
$root = $tree->delete($root, 30);
echo "Inorder traversal after deletion: \n";
$tree->inorder($root);'''