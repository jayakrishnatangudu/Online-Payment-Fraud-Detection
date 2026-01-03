💳 **Online Payment Fraud Detection System**

A machine learning–based web application that classifies online payment transactions as fraudulent or legitimate, trained on real-world transaction data and deployed as an interactive web app.

🚀 **Live Demo**
👉 Live Application: https://online-payment-fraud-detection.streamlit.app/
📂 **Source Code**
👉 GitHub Repository: https://github.com/jayakrishnatangudu/Online-Payment-Fraud-Detection

📌** Problem Statement**
Online payment systems face severe challenges due to extreme class imbalance, where fraudulent transactions are very rare but highly costly if missed.
This project focuses on detecting fraudulent transactions while prioritizing recall to minimize false negatives.

🧠** Approach**
Used PCA-transformed features (V1–V28) to preserve sensitive transaction information
Trained a Decision Tree classifier on an imbalanced dataset
Optimized the model to achieve high recall, which is critical in fraud detection
Deployed the trained model as a real-time web application using Streamlit

📊** Dataset Overview**
Total transactions: 56,961
Fraud cases: 98
Fraud prevalence: 0.17%
Features: 29 numerical features (V1–V28, normAmount)

🧪 **Model Comparison**
Three machine learning models were trained and evaluated on the same test set to compare performance on an extremely imbalanced fraud detection dataset.
| Model               | Accuracy | Precision (Fraud) | Recall (Fraud) | F1 Score | ROC-AUC |
| ------------------- | -------- | ----------------- | -------------- | -------- | ------- |
| Logistic Regression | 97.40%   | 5.77%             | 90%            | 0.11     | 0.94    |
| Decision Tree       | 97.83%   | 7.17%             | 95%            | 0.13     | 0.96    |
| Random Forest       | 99.82%   | 48.65%            | 90%            | 0.63     | 0.95    |

**Confusion Matrices**
The confusion matrices below provide a visual comparison of how each model handles legitimate and fraudulent transactions.
🔹 Logistic Regression

🔹 Decision Tree

🔹 Random Forest

🏆 **Model Selection Rationale**
Although Random Forest achieved the highest overall accuracy and precision, the Decision Tree model was selected for deployment due to the following reasons:
Highest recall (95%), minimizing missed fraudulent transactions
Strong ROC-AUC (0.96), indicating good class separability
Very low inference latency (~1.3 ms), suitable for real-time prediction
Better interpretability compared to ensemble models
This choice reflects a practical trade-off between performance, interpretability, and deployment efficiency.

📈 **Model Performance (Test Set)**
Metric	Value
Accuracy	97.83%
Precision	7.17%
Recall	95%
F1 Score	0.13
ROC-AUC	0.97

⚠️ Note: Precision is low due to extreme class imbalance.
High recall is intentionally prioritized to reduce missed fraudulent transactions, which are more costly than false positives in real-world systems.

⏱️ **Inference Performance**
Average prediction latency: ~1.3 ms per request
Model is loaded once at startup to ensure fast, real-time predictions

⚙️ **Tech Stack**
Language: Python
Libraries: Pandas, NumPy, Scikit-learn
Deployment: Streamlit Cloud

📂** Project Structure**<br>
├── app.py<br>
├── fraud_model.pkl<br>
├── model_metrics.pkl<br>
├── requirements.txt<br>
├── Online_Payment_Fraud_Detection.ipynb<br>
└── README.md<br>

🛠️** Run Locally**
pip install -r requirements.txt
streamlit run app.py




