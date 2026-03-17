from flask import Flask, render_template, request
from predict import predict_fraud

app = Flask(__name__)

# Home page (Input page)
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    # Get data from form
    upi_id = request.form["upi_id"]
    amount = request.form["amount"]

    # Convert amount to float
    amount = float(amount)

    # Get prediction result
    result = predict_fraud(amount)

    # Send result to result page
    return render_template("result.html", 
                           upi=upi_id, 
                           amount=amount, 
                           result=result)

# Run server
if __name__ == "__main__":
    app.run(debug=True)