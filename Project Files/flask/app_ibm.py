import numpy as np
import pickle
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "payments.pkl")
model = pickle.load(open(model_path, "rb"))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    type = request.form['type']
    amount = float(request.form['amount'])
    oldbalanceOrg = float(request.form['oldbalanceOrg'])
    newbalanceOrig = float(request.form['newbalanceOrig'])

    # type.map({"CASH_OUT": 1, "PAYMENT": 2,
    #       "CASH_IN": 3, "TRANSFER": 4,
    #       "DEBIT": 5})
    if type == "CASH_OUT":
        val = 1
    elif type == "PAYMENT":
        val = 2
    elif type == "CASH_IN":
        val = 3
    elif type == "TRANSFER":
        val = 4
    else:
        val = 5

    # Create input array for prediction
    input_array = np.array([[val, amount, oldbalanceOrg, newbalanceOrig]])

    # Make prediction using the loaded model
    prediction = model.predict(input_array)

    # Extract the predicted output value
    output = prediction[0]

    return render_template('predict.html', prediction=output)


if __name__ == '__main__':
    app.run(debug=True)
