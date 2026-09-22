from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
# app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/wanderlust_backend_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Import the blueprints for your routes
from app.routes.destinations_routes import destinations_bp
from app.routes.itineraries_routes import itineraries_bp
from app.routes.expenses_routes import expenses_bp

# Register the blueprints
app.register_blueprint(destinations_bp)
app.register_blueprint(itineraries_bp)
app.register_blueprint(expenses_bp)
