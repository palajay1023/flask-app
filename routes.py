# backend/routes.py
from flask import Blueprint, jsonify, request
from models import PaperRequest
from app import db  # Import db to check connection
from sqlalchemy import text  # Import text function

main = Blueprint('main', __name__)

def create_tables():
    db.create_all()

@main.route('/')
def home():
    return "Greeting from flask backend"


@main.route('/paper_request', methods=['POST'])  # Change method to POST
def request_form(): 
    data = request.get_json()  # Get JSON data from the request
    # Validate and adjust data as needed 
    print(data)
    new_request = PaperRequest(
        title=data['title'],
        link=data['link'],
        start_date=data['start_date'],  # Ensure date format is correct
        end_date=data['end_date'],      # Ensure date format is correct
        comments=data.get('comments', ''),
        whatsapp_number=data['whatsapp_number'],
        country_code=data['country_code']
    )

    db.session.add(new_request)  # Add the new request to the session
    db.session.commit()           # Commit the session to save to the database
    return jsonify({"message": "New paper request added!"}), 201  # Return success message

@main.route('/api/paper-requests', methods=['GET'])  # New route to retrieve all paper requests
def get_paper_requests():
    requests = PaperRequest.query.all()  # Retrieve all entries from the PaperRequest table
    return jsonify([request.to_dict() for request in requests]), 200 

@main.route('/api/test_connection', methods=['GET'])  # New route to test DB connection
def test_connection():
    try:
        # Attempt to execute a simple query
        db.session.execute(text('SELECT 1'))  # Wrap the query with text()
        return jsonify({"message": "Database connection successful!"}), 200
    except Exception as e:
        return jsonify({"message": "Database connection failed!", "error": str(e)}), 500

@main.route('/browse-request', methods=['GET'])
def browse_request():
    requests = PaperRequest.query.all()  # Retrieve all entries from the PaperRequest table
    return jsonify([request.to_dict() for request in requests]), 200