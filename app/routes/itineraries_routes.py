from flask import jsonify, request, Blueprint
from app import db
from app.models import Itinerary

itineraries_bp = Blueprint('itineraries_bp', __name__)

# Create - Add an itinerary activity for a destination
@itineraries_bp.route('/itineraries', methods=['POST'])
def create_itinerary():
    data = request.json
    destination_id = data['destination_id']
    itinerary = Itinerary(destination_id=destination_id, activity=data['activity'])
    db.session.add(itinerary)
    db.session.commit()
    return jsonify({'message': 'Itinerary activity added successfully'})

# Read - Get all itinerary activities for a specific destination
@itineraries_bp.route('/itineraries/<int:destination_id>', methods=['GET'])
def get_itineraries(destination_id):
    itineraries = Itinerary.query.filter_by(destination_id=destination_id).all()
    itinerary_list = []
    for itinerary in itineraries:
        itinerary_dict = {
            'id': itinerary.id,
            'activity': itinerary.activity
        }
        itinerary_list.append(itinerary_dict)
    return jsonify(itinerary_list)

# Update - Update a specific itinerary activity by ID
@itineraries_bp.route('/itineraries/<int:itinerary_id>', methods=['PUT'])
def update_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary is not None:
        data = request.json
        itinerary.activity = data['activity']
        db.session.commit()
        return jsonify({'message': 'Itinerary activity updated successfully'})
    return jsonify({'message': 'Itinerary activity not found'}, 404)

# Delete - Delete a specific itinerary activity by ID
@itineraries_bp.route('/itineraries/<int:itinerary_id>', methods=['DELETE'])
def delete_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary is not None:
        db.session.delete(itinerary)
        db.session.commit()
        return jsonify({'message': 'Itinerary activity deleted successfully'})
    return jsonify({'message': 'Itinerary activity not found'}, 404)
