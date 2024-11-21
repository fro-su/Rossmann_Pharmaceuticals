from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
import sys
sys.path.append('../')

# Create Flask app
app = Flask(__name__)


# Load the serialized model
model_filename = model_filename = r'C:\Users\Firew Ayele\Desktop\kifiya\Rossmann_Pharmaceuticals\notebooks\rf_model_2024-09-24-10-13-30.pkl'
 
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Initialize the scaler used during preprocessing
scaler = StandardScaler()

# Define a route to handle the home request
@app.route('/')
def home():
    return "Welcome to the Store Sales Prediction API!"

# Define API endpoint to receive data and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Extract JSON data from the request
    data = request.get_json(force=True)

    # Convert input data to a DataFrame
    input_data = pd.DataFrame([data])

    # Preprocess the input data (ensure it matches the training data structure)
    input_data_scaled = scaler.transform(input_data)

    # Make prediction using the model
    prediction = model.predict(input_data_scaled)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist()})

# Custom 404 handler to ignore favicon errors
@app.errorhandler(404)
def page_not_found(e):

    # Check if the requested path is 'favicon.ico'
    if 'favicon.ico' in str(e):
        return '', 204  # Return an empty response with status 204 (No Content)
    return jsonify(error="Page not found"), 404  # For other 404 errors

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
