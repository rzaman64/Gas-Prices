import http.client
import json
import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

app = Flask(__name__) 
goo goo
# Replace with your actual API key
#goo goo gaga
load_dotenv()

SECRET_KEY = os.getenv("RAPIDAPI_KEY")
print(SECRET_KEY)

RAPIDAPI_HOST = 'gas-price.p.rapidapi.com'

@app.route('/')
def home():
    return "Gas Price Finder API"

@app.route('/gas-prices', methods=['GET'])
def get_gas_prices():
    # Get state parameter from the request, default to "DE" if not provided
    state = request.args.get('state', 'DE')
    
    # Initialize HTTP connection
    conn = http.client.HTTPSConnection(RAPIDAPI_HOST)
    
    # Set headers for the API request
    headers = {
        'x-rapidapi-key': SECRET_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST
    }
    
    # Make the GET request
    conn.request("GET", f"/stateUsaPrice?state={state}", headers=headers)
    
    # Get the response
    res = conn.getresponse()
    data = res.read()
    
    # Decode and return JSON response
    response_data = data.decode("utf-8")
    try:
        json_data = json.loads(response_data)
        return jsonify(json_data)
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to decode JSON response"}), 500

if __name__ == '__main__':
    app.run(debug=True)
