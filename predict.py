import numpy as np
import pickle

# load model
model = pickle.load(open("fraud_model.pkl", "rb"))

def predict_fraud(amount):

    # model input
    input_data = np.array([[amount]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        return "Fraud Transaction"
    else:
        return "Safe Transaction"