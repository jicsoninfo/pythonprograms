class stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def is_empty(self):
        '''Check if the stack is empty'''
        return len(self.items) == 0
    
    def push(self, item):
        '''Add an item to the top of the stack.'''
        self.items.append(item)

    def pop(self):
        '''Remove and return the top item of the stack, Raise an error if the stack is empty.'''
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Pop from an empty stack')
        
    def display(self):
        '''Display the current items in the stack.'''
        print("Stack:", self.items)

    def size(self):
        '''Return the number of items in the stack'''
        return len(self.items)
    
    def peek(self):
        '''Return the top item of the satck without removing it. Raise an error if the stack is empty.'''
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")
        
    



#Example usage
if __name__ == "__main__":
    stack = stack()

    #push items onto the stack
    stack.push(5)
    stack.push(10)
    stack.push(15)

    print("Current stack:")
    stack.display()

    print("Top item of stack ", stack.peek())
    #print(stack.peek())

    print("Popped item:- ", stack.pop())
    print("Top item after pop:- ", stack.peek())
    print("Is stack empty?", stack.is_empty())

    stack.display()



















































refer01 = '''
class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack. Raise an error if the stack is empty."""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        """Return the top item of the stack without removing it. Raise an error if the stack is empty."""
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def display(self):
        """Display the current items in the stack."""
        print("Stack:", self.items)


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