from flask import Flask, render_template, request, redirect

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('/home')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    upi = request.form.get('upi')
    amount = request.form.get('amount')

    if amount:
        amount = float(amount)
        if amount > 10000:
            result = "FRAUD ❌"
        else:
            result = "SAFE ✅"
    else:
        result = "INVALID INPUT"

    return render_template('result.html', result=result)

if _name_ == '_main_':
    app.run()
