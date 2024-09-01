# app.py
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    data = [float(x) for x in request.form.values()]
    data = np.array([data])

    # Scale the data
    scaled_data = scaler.transform(data)

    # Predict the class
    prediction = model.predict(scaled_data)[0]

    # Map the prediction to the Iris class name
    classes = {0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'}
    predicted_class = classes[prediction]

    return render_template('results.html', prediction=predicted_class)

@app.route('/input',methods=['GET'])
def input():
    return render_template('input.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8000)