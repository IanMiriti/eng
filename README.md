# 🏡 AI-Powered Real Estate Investment Advisor

**AI Spark Hackathon 2025**
**Team: Engineers**

🔗 **Live Application:**
[https://baihvh6z3srni6cmuruicv.streamlit.app/](https://baihvh6z3srni6cmuruicv.streamlit.app/)

🔗 **GitHub Repository:**
[https://github.com/IanMiriti/eng](https://github.com/IanMiriti/eng)

---

## 📌 Project Overview

This project is an **AI-powered Investment Advisor** designed to help users determine whether a house listing in **Istanbul (2020 market)** represents a:

* ✅ **Good Investment Opportunity**
* ⚖️ **Fair / Normal Deal**
* ❌ **Overpriced Property**

Instead of only predicting house prices, the system calculates a **Fair Market Value** and compares it with the **listing price**, providing a **clear investment recommendation**.

This approach directly follows the **AI Spark Hackathon problem statement**.

---

## 🎯 Problem Statement

The Istanbul real estate market shows **high price inconsistency**, making it difficult for fixed-income buyers to decide whether a house is worth its price.

### Our Goal:

To build a **data-driven decision support system** that:

1. Learns 2020 housing market dynamics
2. Predicts a fair property value
3. Classifies listings as **Opportunity / Normal / Expensive**

---

## 📊 Dataset

* **File:** `hackathon_train_set.csv`
* **Year:** 2020
* **Key Constraint Applied:**
  Only properties with
  **`Available for Loan = Yes`**
  were used, as required by the competition rules.

---

## 🧹 Data Preprocessing

### Cleaning

* Removed currency symbols (`TL`), dots, and commas
* Converted price and area fields to numeric values
* Removed rows with missing critical values

### Feature Selection

* Dropped noisy or redundant columns (e.g., neighborhood, advertisement dates)

---

## 🧠 Feature Engineering (Key Innovation)

### Problem Identified

Raw models tend to **over-rely on square meters (m²)** and fail to capture **location quality and market efficiency**.

### Our Solution

We introduced **Target Encoding + Price-per-Area Ratios**:

For key categorical features:

* **District**
* **Number of Rooms**
* **Building Age**

We created:

* Average price per group
* Average **price per gross square meter (PPGSM)**

This allowed the model to learn:

* Neighborhood value
* Structural quality
* Market efficiency

---

## 🤖 Model Selection

### Chosen Model: **XGBoost Regressor**

**Why XGBoost?**

* Excellent performance on tabular data
* Captures non-linear relationships
* Robust against overfitting
* Handles high-dimensional encoded features well

### Evaluation Metrics

* **R² Score**
* **RMSE (Root Mean Squared Error)**

These metrics were selected to ensure both **technical accuracy** and **real-world interpretability**.

---

## 📈 Decision Logic (Business Layer)

Prediction alone is not enough.

We apply a **±10% tolerance margin** around the predicted fair value:

| Condition                        | Classification |
| -------------------------------- | -------------- |
| Listing Price < Fair Value − 10% | 🌟 Opportunity |
| Listing Price within ±10%        | ⚖️ Normal      |
| Listing Price > Fair Value + 10% | 💸 Expensive   |

This reflects **real-world negotiation margins** used in property investment.

---

## 🌐 Web Application (Streamlit)

The system is deployed as an interactive **Streamlit web app** where users can:

* Enter property features
* Input the listing price
* Instantly receive an investment recommendation

### Key Features

* Clean and simple UI
* Real-time predictions
* Clear, investor-friendly output
* No technical knowledge required

---

## 🚀 Deployment (Permanent Access)

The application is **permanently deployed** using **Streamlit Community Cloud**.

### Deployment Steps

1. Exported trained model and app files from Google Colab
2. Uploaded all files to a public GitHub repository
3. Connected the repository to Streamlit Cloud
4. Automatic build using `requirements.txt`
5. App launched with a permanent public URL

✅ No local machine required
✅ 24/7 availability
✅ Fully demo-ready for hackathon evaluation

---

## 📁 Project Structure

```
eng/
├── app.py                      # Streamlit application
├── house_price_model.joblib    # Trained XGBoost model
├── feature_columns.joblib      # Feature blueprint
├── requirements.txt            # Dependencies
├── notebooks/                  # Training notebooks
└── PRESENTATION_REPORT.txt     # Hackathon presentation report
```

---

## 🏆 Hackathon Evaluation Alignment

| Criterion              | Covered |
| ---------------------- | ------- |
| Problem Interpretation | ✅       |
| Data Analysis (EDA)    | ✅       |
| Data Preprocessing     | ✅       |
| Model Selection        | ✅       |
| Model Performance      | ✅       |
| Innovation             | ✅       |
| Applicability          | ✅       |
| Presentation           | ✅       |

---

## 👥 Team

**Team Name:** Engineers

This project was developed as part of the **AI Spark Hackathon**, following all competition rules and constraints.

---

## 📌 Final Note

This is **not just a machine learning model**.
It is a **real-world investment advisor** built with:

* Strong data science principles
* Clear business logic
* Practical usability
* Transparent and reproducible code
