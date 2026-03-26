# Intelligent SMS Spam Detection 📱
**[span_1](start_span)Course:** Fundamentals of Artificial Intelligence & Machine Learning[span_1](end_span)
**[span_2](start_span)Project Category:** Build Your Own Problem (BYOP)[span_2](end_span)
**Author:** SADIYA HASSAN
**[span_3](start_span)Date:** March 2026[span_3](end_span)

---

## 📝 Project Overview
[span_4](start_span)This project addresses the security risks of unsolicited SMS messages, such as phishing attempts designed to steal personal info[span_4](end_span). [span_5](start_span)Using an AI/ML approach, the system distinguishes between legitimate (Ham) and fraudulent (Spam) messages using mathematical probability[span_5](end_span).

### Key Features
* **[span_6](start_span)Supervised Learning:** Maps text strings to a binary output (0 or 1)[span_6](end_span).
* **[span_7](start_span)Naive Bayes Foundation:** Uses Bayes' Theorem to calculate the probability of spam based on word frequency[span_7](end_span).
* **[span_8](start_span)Fast & Lightweight:** Optimized for efficiency, making it practical for mobile devices[span_8](end_span).

## 🛠️ Technical Stack
* **[span_9](start_span)Language:** Python 3.x[span_9](end_span)
* **[span_10](start_span)Libraries:** Scikit-learn (MultinomialNB), Pandas, Matplotlib, Seaborn[span_10](end_span)

## ⚙️ Data Pipeline
[span_11](start_span)[span_12](start_span)The model utilizes the **UCI SMS Spam Collection Dataset** (5,500+ messages)[span_11](end_span)[span_12](end_span).
1. **[span_13](start_span)[span_14](start_span)Cleaning:** Handles Latin-1 encoding and removes unnecessary columns[span_13](end_span)[span_14](end_span).
2. **[span_15](start_span)Vectorization:** Uses `CountVectorizer` to create a **Bag of Words**[span_15](end_span).
3. **[span_16](start_span)[span_17](start_span)Split:** Uses an **80/20 train-test split** to ensure accuracy[span_16](end_span)[span_17](end_span).

## 🚀 How to Run
1. **Clone the repo:**
   `git clone https://github.com/sadiya/sms-spam-detection.git`
2. **Install dependencies:**
   `pip install scikit-learn pandas matplotlib seaborn`
3. **Run the script:**
   `python main.py`

## 📊 Evaluation
[span_18](start_span)The model's performance is verified using a **Confusion Matrix** to ensure no bias despite the data imbalance (more Ham than Spam)[span_18](end_span). We track:
* **[span_19](start_span)Accuracy:** Overall correct predictions[span_19](end_span).
* **[span_20](start_span)Precision:** Accuracy of identified spam[span_20](end_span).
* **[span_21](start_span)Recall:** Proportion of actual spam correctly found[span_21](end_span).
*