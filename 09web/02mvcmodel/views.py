from flask import Blueprint, request, jsonify
from models import SllModel

sll_view = Blueprint('sll_view', __name__)
sll_model = SllModel()

@sll_view.route('/api/nodes', methods=['GET'])
def get_nodes():
    """GET all linked list nodes."""
    nodes = sll_model.get_all_nodes()
    return jsonify({"nodes": nodes})

@sll_view.route('/api/nodes', methods=['POST'])
def create_node():
    """POST a new node to the linked list."""
    data = request.get_json()
    if not data or 'data' not in data:
        return jsonify({"error": "Data field is required"}), 400
    
    node_data = data['data']
    node_id = sll_model.create_node(node_data)
    return jsonify({"message": "Node created", "node_id": str(node_id)}), 201

@sll_view.route('/api/nodes/<node_id>', methods=['PUT'])
def update_node(node_id):
    """PUT (update) an existing node."""
    data = request.get_json()
    if not data or 'data' not in data:
        return jsonify({"error": "Data field is required"}), 400
    
    new_data = data['data']
    updated_count = sll_model.update_node(node_id, new_data)
    
    if updated_count > 0:
        return jsonify({"message": "Node updated"})
    else:
        return jsonify({"error": "Node not found"}), 404

@sll_view.route('/api/nodes/<node_id>', methods=['DELETE'])
def delete_node(node_id):
    """DELETE a node by its ID."""
    deleted_count = sll_model.delete_node(node_id)
    
    if deleted_count > 0:
        return jsonify({"message": "Node deleted"})
    else:
        return jsonify({"error": "Node not found"}), 404
