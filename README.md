# Intelligent SMS Spam Detection 📱
**Course:** Fundamentals of Artificial Intelligence & Machine Learning
**Project Category:** Build Your Own Problem (BYOP)
**Author:** SADIYA HASSAN
**Date:** 28 March 2026

---

## 📝 Project Overview
This project addresses the security risks of unsolicited SMS messages, such as phishing attempts designed to steal personal info Using an AI/ML approach, the system distinguishes between legitimate (Ham) and fraudulent (Spam) messages using mathematical probability.

### Key Features
* **Supervised Learning:** Maps text strings to a binary output (0 or 1).
* **Naive Bayes Foundation:** Uses Bayes' Theorem to calculate the probability of spam based on word frequency.
* **Fast & Lightweight:** Optimized for efficiency, making it practical for mobile devices.

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Libraries:** Scikit-learn (MultinomialNB), Pandas, Matplotlib, Seaborn.

## ⚙️ Data Pipeline
The model utilizes the **UCI SMS Spam Collection Dataset**.
1. **Cleaning:** Handles Latin-1 encoding and removes unnecessary columns.
2. **Vectorization:** Uses `CountVectorizer` to create a **Bag of Words**.
3. **Split:** Uses an **80/20 train-test split** to ensure accuracy.

## 🚀 How to Run
1. **Clone the repo:**
   `https://github.com/sadiyahassan1674-afk/sms-spam-detector.git`
2. **Install dependencies:**
   `pip install scikit-learn pandas matplotlib seaborn`
3. **Run the script:**
   `python main.py`

## 📊 Evaluation
The model's performance is verified using a **Confusion Matrix** to ensure no bias despite the data imbalance (more Ham than Spam).
We track:
* **Accuracy:** Overall correct predictions.
* **Precision:** Accuracy of identified spam.
* **Recall:** Proportion of actual spam correctly found.

