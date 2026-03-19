from flask import Flask, render_template, request, redirect
import pickle
import numpy as np

app = Flask(_name_)

model = pickle.load(open('fraud_model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('/home')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            amount = float(request.form.get('amount'))
            features = np.array([[amount]])
            prediction = model.predict(features)[0]

            result = "Fraud" if prediction == 1 else "Safe"
            return render_template('result.html', result=result)

        except:
            return "Error"

    return render_template('index.html')