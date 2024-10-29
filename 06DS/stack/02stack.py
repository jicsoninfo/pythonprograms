class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        '''Initialize an empty stack.'''
        self.top = None

    def is_empty(self):
        '''Check if the stack is empty'''
        return self.top is None
    
    def push(self, item):
        '''Add an item to the top of the stack.'''
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def display(self):
        '''Display the current items in the stack.'''
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next
        print("Stack:", items)

    def size(self):
        '''Return the number of items in the stack.'''
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def pop(self):
        '''Remove and return the top itetm of the stack, Raise an error if the stack is empty.'''
        if not self.is_empty():
            popped_node = self.top
            self.top = self.top.next
            return popped_node.data
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        """Return the top item of the stack without removing it. Raise an error if the stack is empty."""
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("Peek from an empty stack")
#Example usage

if __name__ == "__main__":
    stack = Stack()

    #push items onto the stack
    stack.push(5)
    stack.push(10)
    stack.push(15)

    print("Currnet Stack:")
    stack.display()
    

    print("Total items in stack:", stack.size())
    print("Popped item:", stack.pop())
    print("Is stack empty?", stack.is_empty())
    print("Top item after pop:", stack.peek())













































refer01 = '''

=====================================================================
through linked list
class Node:
    def __init__(self, data):
        """Initialize a node with data and a reference to the next node."""
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.top = None

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def push(self, item):
        """Add an item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Remove and return the top item of the stack. Raise an error if the stack is empty."""
        if not self.is_empty():
            popped_node = self.top
            self.top = self.top.next
            return popped_node.data
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        """Return the top item of the stack without removing it. Raise an error if the stack is empty."""
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        """Return the number of items in the stack."""
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        """Display the current items in the stack."""
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next
        print("Stack:", items)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    # Push items onto the stack
    stack.push(5)
    stack.push(10)
    stack.push(15)
    
    print("Current stack:")
    stack.display()

    print("Popped item:", stack.pop())
    print("Top item after pop:", stack.peek())
    print("Is stack empty?", stack.is_empty())
    
    stack.display()

'''