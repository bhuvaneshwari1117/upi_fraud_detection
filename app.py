from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('fraud_model.pkl', 'rb'))

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

if __name__ == "__main__":
    app.run()

    
