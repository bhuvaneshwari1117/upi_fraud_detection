import numpy as np
import pickle

# Load trained model
model = pickle.load(open("fraud_model.pkl", "rb"))

def predict_fraud(amount):
    try:
        # Convert input to numpy array
        input_data = np.array([[amount]])

        # Prediction
        prediction = model.predict(input_data)

        # Result
        if prediction[0] == 1:
            return "Fraud"
        else:
            return "Safe"

    except Exception as e:
        return "Error"