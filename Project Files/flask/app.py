"""
Online Payments Fraud Detection - Flask Application

This Flask app provides a web interface for fraud detection predictions.
Routes:
    /          -> home.html (Home page)
    /predict   -> predict.html (Input form)
    /submit    -> submit.html (Prediction result)
"""

import numpy as np
import os
from flask import Flask, render_template, request
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model saved with joblib
model_path = os.path.join(os.path.dirname(__file__), "payments.pkl")

try:
    model = joblib.load(model_path)
    print(f"Model loaded successfully from {model_path}")
except FileNotFoundError:
    print(f"ERROR: Model file not found at {model_path}")
    print("Please run the training notebook first to generate payments.pkl")
    model = None


def predict_fraud(step, type_val, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest):
    """
    Predict fraud for given transaction parameters.
    
    Parameters:
    -----------
    step : int
        Time step (1 step = 1 hour)
    type_val : int
        Transaction type (1=CASH_OUT, 2=PAYMENT, 3=CASH_IN, 4=TRANSFER, 5=DEBIT)
    amount : float
        Transaction amount
    oldbalanceOrg : float
        Original account balance before transaction
    newbalanceOrig : float
        Original account balance after transaction
    oldbalanceDest : float
        Destination account balance before transaction
    newbalanceDest : float
        Destination account balance after transaction
    
    Returns:
    --------
    str : 'Fraud' or 'Not Fraud'
    """
    if model is None:
        return "Error: Model not loaded"
    
    # Create input array in the same order as training features
    # Features: ['step', 'type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
    input_array = np.array([[step, type_val, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])
    
    # Make prediction
    prediction = model.predict(input_array)
    
    # Convert prediction to readable format
    # Model outputs 0 for No Fraud, 1 for Fraud
    if prediction[0] == 0:
        return "Not Fraud"
    else:
        return "Fraud"


@app.route('/')
def home():
    """Home page route"""
    return render_template('home.html')


@app.route('/predict')
def predict():
    """Predict page route - shows input form"""
    return render_template('predict.html')


@app.route('/submit', methods=['POST'])
def submit():
    """Submit route - processes form data and returns prediction"""
    try:
        # Get form data
        step = int(request.form.get('step', 1))
        type_val = int(request.form.get('type', 2))
        amount = float(request.form.get('amount', 0))
        oldbalanceOrg = float(request.form.get('oldbalanceOrg', 0))
        newbalanceOrig = float(request.form.get('newbalanceOrig', 0))
        oldbalanceDest = float(request.form.get('oldbalanceDest', 0))
        newbalanceDest = float(request.form.get('newbalanceDest', 0))
        
        # Make prediction
        prediction = predict_fraud(
            step, type_val, amount, 
            oldbalanceOrg, newbalanceOrig,
            oldbalanceDest, newbalanceDest
        )
        
        # Pass prediction to submit.html
        return render_template('submit.html', prediction=prediction)
        
    except Exception as e:
        error_message = f"Error processing request: {str(e)}"
        return render_template('submit.html', prediction=f"Error: {error_message}")


if __name__ == '__main__':
    print("\n" + "="*50)
    print("Online Payments Fraud Detection - Flask App")
    print("="*50)
    print(f"Model path: {model_path}")
    print(f"Model loaded: {model is not None}")
    print("\nStarting Flask server...")
    print("Access the application at: http://127.0.0.1:5000")
    print("="*50 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)
