Online Payments Fraud Detection
A comprehensive machine learning project for detecting fraudulent online payment transactions using advanced ML algorithms.

📋 Project Overview
This project implements a complete fraud detection system that analyzes transaction data to identify potentially fraudulent payments. The system uses multiple machine learning algorithms including Decision Trees, Random Forest, SVM, and Extra Trees Classifiers to achieve high accuracy in fraud detection.

Key Features
Real-time Fraud Detection: Web-based interface for instant fraud prediction
Multiple ML Models: Comparison of 4 different algorithms
Comprehensive Analysis: Univariate, bivariate, and descriptive analysis
Hyperparameter Tuning: Optimized model performance
Production Ready: Flask-based web application
🔄 Project Flow
1. Data Collection
Dataset: PS_20174392719_1491204439457_logs.csv
Contains transaction records with features like amount, account balances, transaction type, etc.
2. Data Preprocessing
Remove unnecessary columns: Removed identifier columns (nameOrig, nameDest)
Handle null values: Checked and verified no null values
Univariate Analysis:
Distribution of transaction amounts
Transaction type distribution
Fraud vs Non-Fraud distribution
Bivariate Analysis:
Fraud rate by transaction type
Amount distribution comparison
Correlation analysis
Descriptive Analysis:
Statistical summaries
Fraud percentage
Transaction type statistics
3. Model Building
Models Trained:
Decision Tree Classifier
Random Forest Classifier
Support Vector Machine (SVM)
Extra Trees Classifier
Process:
Feature encoding (categorical to numerical)
Train/Test split (80/20)
Model training and evaluation
Accuracy comparison
Best model selection
4. Hyperparameter Tuning
Grid Search CV for optimal parameters
Cross-validation for robust evaluation
Final model optimization
5. Model Evaluation
Accuracy metrics
Classification report
Confusion matrix
Precision, Recall, F1-score
6. Model Deployment
Saved as payments.pkl in both flask/ and training/ directories
Flask web application for predictions
📁 Folder Structure
online_payments_fraud_detection/
│
├── data/
│   └── PS_20174392719_1491204439457_logs.csv
│
├── flask/
│   ├── templates/
│   │   ├── home.html
│   │   ├── predict.html
│   │   └── submit.html
│   │
│   ├── app.py
│   └── payments.pkl
│
├── training/
│   ├── ONLINE_PAYMENTS_FRAUD_DETECTION.ipynb
│   └── payments.pkl
│
├── training_ibm/
│   └── online_payments_fraud_prediction_using_ibm.ipynb
│
├── requirements.txt
└── README.md
🤖 Model Details
Features Used:
step: Time step (1 step = 1 hour)
type: Transaction type (1=CASH_OUT, 2=PAYMENT, 3=CASH_IN, 4=TRANSFER, 5=DEBIT)
amount: Transaction amount
oldbalanceOrg: Original account balance before transaction
newbalanceOrig: Original account balance after transaction
oldbalanceDest: Destination account balance before transaction
newbalanceDest: Destination account balance after transaction
Target Variable:
isFraud: Binary classification (0 = No Fraud, 1 = Fraud)
Model Performance:
Multiple models are trained and compared
Best performing model is selected based on accuracy
Hyperparameter tuning optimizes the final model
Model achieves high accuracy in fraud detection
🚀 How to Run
Prerequisites
Python 3.8 or higher
pip package manager
Step 1: Install Dependencies
pip install -r requirements.txt
Step 2: Train the Model (Optional)
If you want to retrain the model:

# Open and run the Jupyter notebook
jupyter notebook training/ONLINE_PAYMENTS_FRAUD_DETECTION.ipynb
This will generate payments.pkl files in both flask/ and training/ directories.

Step 3: Run Flask Application
cd flask
python app.py
The application will start on http://127.0.0.1:5000

Step 4: Access the Web Interface
Home Page (/): Project overview and navigation
Predict Page (/predict): Input form for transaction details
Submit Page (/submit): Shows prediction result
📸 Application Screenshots Explanation
Home Page
Light blue gradient background with subtle pattern overlay
Top right navigation buttons: Home and Predict
Centered title: "Online Payments Fraud Detection"
Project description: Overview of the system
Action buttons: Start Prediction and Learn More
Predict Page
Input form with the following fields:
Step (time step)
Type (transaction type dropdown)
Amount
OldbalanceOrg
NewbalanceOrig
OldbalanceDest
NewbalanceDest
Submit button at the bottom left
Help text explaining the input requirements
Submit Page
Prediction result display:
Shows: "The predicted fraud for the online payment is [Fraud/Not Fraud]"
Color-coded result (Red for Fraud, Green for Not Fraud)
Action buttons: Predict Another and Back to Home
🛠️ Technologies Used
Python: Core programming language
Flask: Web framework
Pandas: Data manipulation and analysis
NumPy: Numerical computations
Scikit-learn: Machine learning algorithms
Matplotlib & Seaborn: Data visualization
Jupyter Notebook: Interactive development
HTML/CSS: Web interface
📊 Data Analysis Highlights
Dataset Size: 6,362,620 transactions
Fraud Rate: Very low (highly imbalanced dataset)
Transaction Types: CASH_OUT, PAYMENT, CASH_IN, TRANSFER, DEBIT
Key Insights:
TRANSFER and CASH_OUT transactions show higher fraud rates
Amount and balance changes are strong indicators
Correlation analysis reveals important feature relationships
🔍 Model Comparison
The project compares multiple algorithms:

Decision Tree: Fast, interpretable
Random Forest: Robust, handles overfitting well
SVM: Good for complex boundaries
Extra Trees: Similar to Random Forest, often faster
The best performing model is selected based on accuracy and deployed.

📝 Notes
The model file (payments.pkl) must exist in the flask/ directory for the app to run
If the model file is missing, run the training notebook first
The application uses a POST method for form submission
All predictions are made in real-time
👨‍💻 Development
Project Structure Benefits:
Separation of concerns: Training code separate from deployment
Modularity: Easy to update models without changing app code
Scalability: Can easily add new features or models
Maintainability: Clear folder structure
📄 License
This project is developed as part of SmartBridge Internship Program.

🙏 Acknowledgments
Dataset: Online Payments Fraud Detection Dataset
Libraries: Scikit-learn, Flask, Pandas, NumPy communities
Note: This is a production-ready implementation with complete error handling, clean code structure, and comprehensive documentation.
