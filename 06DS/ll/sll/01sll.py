# from flask import Flask
# app = Flask(__name__)

# class NodeSll:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Sll:
#     def __init__(self):
#         '''Initialize an empty list.'''
#         self.head = None

#     def sll_add_front(self, data):
#         newnodesll = NodeSll(data)
#         newnodesll.next = self.head
#         self.head = newnodesll

#     def sll_print(self):
#         if self.head is None:
#             print("List is empty")
#             return("List is empty")
#         else:
#             temp = self.head
#             # while temp is not None:
#             #     print(temp.data)
#             #     temp = temp.next
#             result = []
#             while temp:
#                 result.append(str(temp.data))  # Collect data as strings
#                 temp = temp.next
#             return " -> ".join(result)

#     def sll_push_back(self, data):
#         newnodesll = NodeSll(data)
#         if self.head is None:
#             self.head = newnodesll
#             return
#         else:
#             temp = self.head
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = newnodesll

            
            

# # Method to define how the list is printed
#     def __str__(self):
#         elements = []
#         current = self.head
#         while current:
#             elements.append(str(current.data))  # Add node data to the list
#             current = current.next
#         return " -> ".join(elements)  # Return the joined string of node data

#     # Custom method to mimic PHP's print_r()
#     def print_r(self):
#         elements = []
#         current = self.head
#         while current:
#             elements.append(str(current.data))  # Add node data to the list
#             current = current.next
#         print("Linked List: " + " -> ".join(elements))  # Mimic print_r() output style



# newsingle = Sll()
# newsingle.sll_add_front(10)
# newsingle.sll_add_front(15)
# newsingle.sll_add_front(20)
# newsingle.sll_add_front(25)

# newsingle.sll_push_back(30)
# newsingle.sll_push_back(35)
# newsingle.sll_push_back(40)
# newsingle.sll_push_back(45)


# newsingle.sll_print()

# newsingle.print_r() 

# print(newsingle)
# # import pprint
# # pprint(newsingle)

# @app.route('/')
# def home():
#     # Print the list when the home route is accessed
#     return f"Linked List: {newsingle.sll_print()}"


# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, render_template, request, make_response, jsonify

app = Flask(__name__)

class NodeSll:
    def __init__(self, data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        '''Initialize an empty list.'''
        self.head = None

    def sll_add_front(self, data):
        newnodesll = NodeSll(data)
        newnodesll.next = self.head
        self.head = newnodesll

    def sll_print(self):
        if self.head is None:
            return "List is empty"
        else:
            temp = self.head
            result = []
            while temp:
                result.append(str(temp.data))
                temp = temp.next
            return " -> ".join(result)

    def sll_push_back(self, data):
        newnodesll = NodeSll(data)
        if self.head is None:
            self.head = newnodesll
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnodesll

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

    def print_r(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Linked List: " + " -> ".join(elements))


newsingle = Sll()
newsingle.sll_add_front(10)
newsingle.sll_add_front(15)
newsingle.sll_add_front(20)
newsingle.sll_add_front(25)

newsingle.sll_push_back(30)
newsingle.sll_push_back(35)
newsingle.sll_push_back(40)
newsingle.sll_push_back(45)

@app.route('/')
def home():
    # Check if the user has a theme set
    theme = request.cookies.get('theme', 'light')  # Default to light mode
    return render_template('index.html', theme=theme, linked_list=newsingle.sll_print())

@app.route('/toggle_theme')
def toggle_theme():
    # Get the current theme from the cookies
    current_theme = request.cookies.get('theme', 'light')

    # Toggle the theme
    new_theme = 'dark' if current_theme == 'light' else 'light'

    # Set the new theme in cookies
    resp = make_response(render_template('index.html', theme=new_theme, linked_list=newsingle.sll_print()))
    resp.set_cookie('theme', new_theme)

    return resp

if __name__ == "__main__":
    app.run(debug=True)
