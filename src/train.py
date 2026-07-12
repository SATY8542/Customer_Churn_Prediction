import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)
from preprocess import load_data

# Load processed dataset
X_train, X_test, y_train, y_test = load_data("data/customer_churn.csv")

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("Customer Churn Prediction Model")
print("=" * 50)

print(f"\nAccuracy : {accuracy * 100:.2f}%")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Save trained model
joblib.dump(model, "models/churn_model.pkl")

print("\nModel saved successfully!")
print("Location : models/churn_model.pkl")