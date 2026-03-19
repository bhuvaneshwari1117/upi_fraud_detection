from flask import Flask, render_template, request, redirect
import pickle
import numpy as np

app = Flask(__name__)

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
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
