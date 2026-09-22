from flask import Blueprint
destinations_bp = Blueprint('destinations_bp', __name__)
itineraries_bp = Blueprint('itineraries_bp', __name__)
expenses_bp = Blueprint('expenses_bp', __name__)

# Import the route files
from . import destinations_routes, itineraries_routes, expenses_routes
