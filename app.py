from flask import Flask, render_template, request, redirect

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('/predict')
    return render_template('login.html')

@app.route('/predict')
def predict():
    return render_template('index.html')

if _name_ == '_main_':
    app.run()
    
