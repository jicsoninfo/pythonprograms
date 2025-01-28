# import http.server
# import socketserver
# import os

# # Change the directory to the folder where your HTML, CSS files are stored
# os.chdir("09web/01darkmode")  # Make sure you're in the correct folder

# # Define the handler to serve the files
# Handler = http.server.SimpleHTTPRequestHandler

# # Set the port and start the server
# PORT = 8000
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"Serving at port {PORT}")
#     httpd.serve_forever()




import http.server
import socketserver
import os
import urllib

# Linked List Implementation
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


# Initialize the Linked List
newsingle = Sll()
newsingle.sll_add_front(10)
newsingle.sll_add_front(15)
newsingle.sll_add_front(20)
newsingle.sll_add_front(25)

newsingle.sll_push_back(30)
newsingle.sll_push_back(35)
newsingle.sll_push_back(40)
newsingle.sll_push_back(45)

# Python function to serve the linked list data
def get_linked_list_data():
    return newsingle.sll_print()

# Handler to serve the HTML page and linked list data
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Handle the request and return an HTML page
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Render the linked list data dynamically in the HTML page
            linked_list_data = get_linked_list_data()
            with open('index.html', 'r') as file:
                html_content = file.read()
                html_content = html_content.replace("{{ linked_list }}", linked_list_data)
                self.wfile.write(html_content.encode())
        else:
            # If the request is not for the root, let the default handler serve the static file
            super().do_GET()

# Change the directory to the folder where your HTML, CSS files are stored
os.chdir("09web/01darkmode")  # Make sure you're in the correct folder

# Set the port and start the server
PORT = 8090
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

