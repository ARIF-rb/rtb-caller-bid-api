from flask import Flask, request, render_template, jsonify
import requests
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Retreaver API credentials
API_KEY = "5465d0b5-97b7-413d-a798-a23467b0b321"
SOURCE_ID = "KSH"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_bid', methods=['GET'])
def get_bid():
    caller_number = request.args.get("caller_number")
    
    if not caller_number:
        return jsonify({"error": "Missing caller_number"}), 400
    
    url = f"https://rtb.retreaver.com/rtbs.json?key={API_KEY}&source_id={SOURCE_ID}&caller_number={caller_number}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        bid_data = response.json()
    
        logging.info(f"API Response: {bid_data}")
        
        return render_template("index.html", bid_data=bid_data, caller_number=caller_number)
    
    except requests.exceptions.RequestException as e:
        logging.error(f"API Request failed: {e}")
        return render_template("index.html", error="Failed to retrieve bid. Please try again later.")

if __name__ == "__main__":
    app.run(debug=True)
