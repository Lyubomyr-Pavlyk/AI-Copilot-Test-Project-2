from flask import jsonify, request, Blueprint
from app import db
from app.models import Destination

destinations_bp = Blueprint('destinations_bp', __name__)

# Read - Get all destinations
@destinations_bp.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    destination_list = []
    for destination in destinations:
        destination_dict = {
            'id': destination.id,
            'name': destination.name,
            'description': destination.description,
            'location': destination.location
        }
        destination_list.append(destination_dict)
    return jsonify(destination_list)


# Create - Add a new destination
@destinations_bp.route('/destinations', methods=['POST'])
def create_destination():
    data = request.json
    destination = Destination(name=data['name'], description=data.get('description'), location=data.get('location'))
    db.session.add(destination)
    db.session.commit()
    return jsonify({'message': 'Destination created successfully'})

# Read - Get a specific destination by ID
@destinations_bp.route('/destinations/<int:destination_id>', methods=['GET'])
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination is not None:
        destination_data = {
            'id': destination.id,
            'name': destination.name,
            'description': destination.description,
            'location': destination.location
        }
        return jsonify(destination_data)
    return jsonify({'message': 'Destination not found'}, 404)

# Update - Update a specific destination by ID
@destinations_bp.route('/destinations/<int:destination_id>', methods=['PUT'])
def update_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination is not None:
        data = request.json
        destination.name = data['name']
        destination.description = data.get('description')
        destination.location = data.get('location')
        db.session.commit()
        return jsonify({'message': 'Destination updated successfully'})
    return jsonify({'message': 'Destination not found'}, 404)

# Delete - Delete a specific destination by ID
@destinations_bp.route('/destinations/<int:destination_id>', methods=['DELETE'])
def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination is not None:
        db.session.delete(destination)
        db.session.commit()
        return jsonify({'message': 'Destination deleted successfully'})
    return jsonify({'message': 'Destination not found'}, 404)
