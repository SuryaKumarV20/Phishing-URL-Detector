🛡️ Phishing URL Detector

A machine learning-based system that detects phishing websites from URLs using NLP and classification algorithms. This project helps enhance cybersecurity by identifying malicious links before they can harm users.

🚀 Features

✅ Extracts important features from URLs (length, special characters, domain info, etc.)
✅ Uses ML algorithms (Logistic Regression, Random Forest, SVM, etc.)
✅ Classifies URLs as Legitimate ✅ or Phishing ❌
✅ Supports batch prediction and real-time testing
✅ Easy-to-use script with modular code structure

🛠️ Tech Stack

Python 🐍

Scikit-learn (ML models)

Pandas, NumPy (data preprocessing)

Matplotlib, Seaborn (visualization)

Joblib (model persistence)

📂 Project Structure
Phishing-URL-Detector/
│── dataset/               # Training datasets (legitimate + phishing URLs)  
│── phishing_detector.py   # Main model training script  
│── feature_extraction.py  # Extract features from URLs  
│── predict.py             # Test model with new URLs  
│── requirements.txt       # Dependencies  
│── README.md              # Project documentation  
│── saved_model.pkl        # Trained ML model  

⚙️ Installation & Setup

1️⃣ Clone the repo

git clone https://github.com/your-username/Phishing-URL-Detector.git
cd Phishing-URL-Detector


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run training

python phishing_detector.py


4️⃣ Test prediction

python predict.py "http://suspicious-example.com/login"

📊 Model Performance

Accuracy: ~95%

Precision & Recall optimized for phishing detection

Tested on legitimate + phishing datasets

🔮 Future Improvements

Add deep learning models (RNN/LSTM for URL sequences)

Deploy as a Flask/Django Web App

Integrate with a browser extension for real-time detection

API endpoint for other applications

🤝 Contributing

Pull requests are welcome! If you’d like to add improvements, open an issue first.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Surya Kumar V

🌐 LinkedIn

✉️ Email
