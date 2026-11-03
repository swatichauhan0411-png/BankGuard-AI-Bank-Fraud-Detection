from flask import Flask, render_template, request
import joblib
import uuid
import pandas as pd

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load("Model/fraud_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    message = None
    transaction_id = None

    if request.method == "POST":
        try:
            transaction = pd.DataFrame([{
                "step": int(request.form["step"]),
                "type": request.form["type"],
                "amount": float(request.form["amount"]),
                "oldbalanceOrg": float(request.form["oldbalanceOrg"]),
                "newbalanceOrig": float(request.form["newbalanceOrig"]),
                "oldbalanceDest": float(request.form["oldbalanceDest"]),
                "newbalanceDest": float(request.form["newbalanceDest"])
            }])

            result = model.predict(transaction)[0]

            if result == 1:
                prediction = "Potential Fraud Transaction"
                message = "The model has classified this transaction as potentially fraudulent."
            else:
                prediction = "Likely Normal Transaction"
                message = "The model has classified this transaction as likely normal."

        except ValueError:
            prediction = "Invalid Input"
            message = "Please enter valid numeric values."

    if prediction:
        transaction_id = "TXN-" + uuid.uuid4().hex[:8].upper()

    return render_template(
        "index.html",
        prediction=prediction,
        message=message,
        transaction_id=transaction_id
    )


if __name__ == "__main__":
    app.run(debug=True)
