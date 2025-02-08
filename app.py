# app.py
from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Path to the CSV file
CSV_FILE = 'data.csv'

def read_csv():
    """Read data from the CSV file using Pandas and return it as a list of dictionaries."""
    if not os.path.exists(CSV_FILE):
        return []
    df = pd.read_csv(CSV_FILE)
    return df.to_dict(orient='records')

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Flask API in Docker!'})

@app.route('/users', methods=['GET'])
def get_users():
    """Endpoint to fetch all users."""
    users = read_csv()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Endpoint to fetch a specific user by ID."""
    users = read_csv()
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)