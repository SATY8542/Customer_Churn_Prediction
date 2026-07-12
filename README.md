# 📊 Customer Churn Prediction

A Machine Learning project that predicts whether a customer is likely to leave (churn) or continue using a company's service. This project uses classification algorithms and provides an interactive web application built with **Streamlit**.

---

# 🚀 Features

- Predict customer churn
- User-friendly Streamlit interface
- Data preprocessing and cleaning
- Feature encoding and scaling
- Machine Learning model training
- Model performance evaluation
- Single customer prediction
- Confidence score for predictions
- Saved trained model using Joblib

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

# 📂 Project Structure

```
Customer_Churn_Prediction/
│
├── data/
│   └── customer_churn.csv
│
├── models/
│   └── churn_model.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

The dataset contains customer information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Contract Type
- Monthly Charges
- Total Charges

**Target Variable**

- Churn (Yes / No)

---

# 🤖 Machine Learning Algorithm

- Decision Tree Classifier

*(You can also experiment with Logistic Regression, Random Forest, XGBoost, or SVM for comparison.)*

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SATY8542/Customer_Churn_Prediction.git
```

Move to the project folder

```bash
cd Customer_Churn_Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Train the Model

```bash
python src/train.py
```

This creates:

```
models/churn_model.pkl
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

# 📈 Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. Feature Encoding
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Save Model
9. Predict Customer Churn

---

# 📊 Model Evaluation

Metrics used:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 📸 Application Preview

### Home Page

- Enter customer details
- Click **Predict**
- View prediction result

### Example

```
Input:
Tenure = 12
Monthly Charges = 75
Contract = Month-to-Month

Prediction:
Customer is likely to Churn

Confidence:
94%
```

---

# 🔮 Future Improvements

- Batch CSV Prediction
- Model Comparison Dashboard
- Feature Importance Graph
- ROC Curve
- SHAP Explainability
- Streamlit Cloud Deployment
- Download Prediction Results

---

# 📦 Requirements

```
pandas
numpy
scikit-learn
matplotlib
streamlit
joblib
```

---

# 👨‍💻 Author

**Satyendra Singh**

GitHub:
https://github.com/SATY8542

LinkedIn:
(Add your LinkedIn profile here)

---

# 📄 License

This project is created for educational and learning purposes.