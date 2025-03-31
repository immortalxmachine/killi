from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:adhi@localhost/apartment_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def execute_query(query, params=None):
    with db.engine.connect() as connection:
        connection.execute(query, params or ())

def fetch_results(query, params=None):
    with db.engine.connect() as connection:
        result = connection.execute(query, params or ())
        return [dict(row) for row in result]

class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apartment_no = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    rent = db.Column(db.Float, nullable=False)

class Resident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'), nullable=False)
    lease_start = db.Column(db.Date, nullable=False)
    lease_end = db.Column(db.Date, nullable=False)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class MaintenanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'), nullable=False)
    issue_description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

class RentPayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resident_id = db.Column(db.Integer, db.ForeignKey('resident.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'), nullable=False)
    purpose = db.Column(db.String(255), nullable=False)

# Removed JavaScript code as it does not belong in a Python file.