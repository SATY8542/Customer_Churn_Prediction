import joblib
import pandas as pd

model = joblib.load("models/churn_model.pkl")

sample = pd.DataFrame([{
    "CreditScore":600,
    "Age":35,
    "Balance":50000,
    "EstimatedSalary":60000
}])

prediction = model.predict(sample)

print("Prediction:", prediction[0])