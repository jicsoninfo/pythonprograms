from pymongo import MongoClient

# Database setup
client = MongoClient("mongodb://localhost:27017/")
db = client.mydatabase  # Use your database name here

# Linked List Node model for demonstration purposes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SllModel:
    def __init__(self):
        self.collection = db["linked_list"]  # MongoDB collection to store linked list data

    def create_node(self, data):
        """Add a node to the linked list."""
        node = {"data": data, "next": None}
        result = self.collection.insert_one(node)
        return result.inserted_id

    def get_all_nodes(self):
        """Get all nodes from the linked list collection."""
        nodes = self.collection.find()
        return [node['data'] for node in nodes]

    def update_node(self, node_id, new_data):
        """Update node data by ID."""
        result = self.collection.update_one(
            {"_id": node_id},
            {"$set": {"data": new_data}}
        )
        return result.modified_count

    def delete_node(self, node_id):
        """Delete a node by ID."""
        result = self.collection.delete_one({"_id": node_id})
        return result.deleted_count
