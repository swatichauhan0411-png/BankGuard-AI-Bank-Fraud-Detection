# 🏦 BankGuard AI – Bank Fraud Detection System

An AI-Based Bank Fraud Detection System built using Machine Learning and Flask to identify potentially fraudulent financial transactions.

## 📌 Project Overview

BankGuard AI is a machine learning-based academic project designed to classify financial transactions as potentially fraudulent or likely normal.

The system uses a **Random Forest Classifier** trained on the PaySim synthetic financial transaction dataset. A Flask-based web application provides a simple dashboard where users can enter transaction details and view the model's prediction.

## 🎯 Project Objectives

- Identify potentially fraudulent transactions using machine learning.
- Apply data preprocessing and classification techniques.
- Develop a user-friendly web interface using Flask.
- Demonstrate how machine learning can support financial transaction analysis.

## ✨ Key Features

- Machine learning-based transaction classification.
- Random Forest classification model.
- Interactive web dashboard.
- Transaction input form.
- Fraud and normal prediction results.
- Unique transaction reference ID for each submitted prediction.
- Dark-themed responsive interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning |
| Random Forest | Classification algorithm |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | User interface design |
| Joblib | Model saving and loading |

## 📂 Project Structure

```text
BankGuard-AI-Bank-Fraud-Detection/
│
├── Model/
│   └── fraud_model.pkl
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── base.html
│   └── index.html
│
├── app.py
├── inspect_dataset.py
├── prepare_data.py
├── train_model.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/swatichauhan0411-png/BankGuard-AI-Bank-Fraud-Detection.git
```

**2. Open the project folder**

```bash
cd BankGuard-AI-Bank-Fraud-Detection
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Run the Flask application**

```bash
python app.py
```

**5. Open the application**

Visit this address in your browser:

```text
http://127.0.0.1:5000
```

## 📊 Dataset Information

This project uses the PaySim synthetic financial transaction dataset.

The dataset contains transaction information such as:

- Transaction type
- Transaction amount
- Sender's previous and new balance
- Receiver's previous and new balance
- Fraud classification label

The original dataset is not included in this repository because of its large file size.

## 🤖 Machine Learning Model

- Algorithm: Random Forest Classifier
- Problem Type: Binary Classification
- Target Variable: `isFraud`
- Data Split: 80% Training and 20% Testing
- Model Persistence: Joblib

## 🔮 Future Enhancements

- Add transaction history.
- Improve model evaluation and performance.
- Add graphical transaction analytics.
- Develop an administrator dashboard.
- Explore real-time transaction monitoring.

## ⚠️ Disclaimer

This is an academic demonstration project developed using synthetic financial transaction data. It is not connected to any real banking system and should not be used as a production fraud detection solution.

## 👩‍💻 Project Information

**Project Name:** BankGuard AI – Bank Fraud Detection System

**Domain:** Artificial Intelligence and Machine Learning

**Application Type:** Web-Based Machine Learning Application

**GitHub Repository:** https://github.com/swatichauhan0411-png/BankGuard-AI-Bank-Fraud-Detection

---

⭐ If you find this project interesting, feel free to explore the repository!
