from flask import Flask, render_template, request
import pickle
import os

app = Flask(_name_)

model_path = os.path.join(os.path.dirname(_file_), 'fraud_model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/predict', methods=['POST'])
def predict():
    upi = request.form['upi']
    amount = float(request.form['amount'])

    prediction = model.predict([[amount]])

    if prediction[0] == 1:
        result = "Fraud ❌"
    else:
        result = "Safe ✅"

    return render_template('result.html', result=result)

    
