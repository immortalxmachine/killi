from flask import Blueprint, request, jsonify, render_template
from .database import execute_query, fetch_results

app = Blueprint('main', __name__)

@app.route('/')
def index():
    return render_template('killi3.html')

@app.route('/manage_maintenance', methods=['POST'])
def manage_maintenance():
    data = request.get_json()
    apartment_id = data.get('apartment_id')
    issue_description = data.get('issue_description')
    query = "INSERT INTO maintenance_requests (apartment_id, issue_description) VALUES (%s, %s)"
    execute_query(query, (apartment_id, issue_description))
    return jsonify({'message': 'Maintenance Request Added/Updated!'}), 201

@app.route('/manage_payment', methods=['POST'])
def manage_payment():
    data = request.get_json()
    resident_id = data.get('resident_id')
    amount = data.get('amount')
    query = "INSERT INTO rent_payments (resident_id, amount) VALUES (%s, %s)"
    execute_query(query, (resident_id, amount))
    return jsonify({'message': 'Payment Recorded!'}), 201

@app.route('/manage_visitor', methods=['POST'])
def manage_visitor():
    data = request.get_json()
    name = data.get('name')
    contact = data.get('contact')
    apartment_id = data.get('apartment_id')
    query = "INSERT INTO visitors (name, contact, apartment_id) VALUES (%s, %s, %s)"
    execute_query(query, (name, contact, apartment_id))
    return jsonify({'message': 'Visitor Added/Updated!'}), 201

@app.route('/apartments', methods=['GET'])
def get_apartments():
    apartments = fetch_results("SELECT * FROM apartments")
    return jsonify(apartments)

@app.route('/residents', methods=['GET'])
def get_residents():
    residents = fetch_results("SELECT * FROM residents")
    return jsonify(residents)

@app.route('/staff', methods=['GET'])
def get_staff():
    staff = fetch_results("SELECT * FROM staff")
    return jsonify(staff)

@app.route('/maintenance_requests', methods=['GET'])
def get_maintenance_requests():
    requests = fetch_results("SELECT * FROM maintenance_requests")
    return jsonify(requests)

@app.route('/rent_payments', methods=['GET'])
def get_rent_payments():
    payments = fetch_results("SELECT * FROM rent_payments")
    return jsonify(payments)

@app.route('/visitors', methods=['GET'])
def get_visitors():
    visitors = fetch_results("SELECT * FROM visitors")
    return jsonify(visitors)