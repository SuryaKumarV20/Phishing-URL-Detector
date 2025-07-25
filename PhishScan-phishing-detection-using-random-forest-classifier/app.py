from flask import Flask, render_template, request
import whois
from urllib.parse import urlparse
import datetime

app = Flask(__name__)

def extract_url_features(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc
        w = whois.whois(domain)

        creation_date = w.creation_date
        expiration_date = w.expiration_date

        # Handle possible list return types
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        if creation_date and expiration_date:
            domain_expiration_days = (expiration_date - datetime.datetime.now()).days
        else:
            domain_expiration_days = "Unavailable"

        return {
            "url": url,
            "domain_name": w.domain_name if w.domain_name else "Unavailable",
            "registrar": w.registrar if w.registrar else "Unavailable",
            "creation_date": creation_date if creation_date else "Unavailable",
            "expiration_date": expiration_date if expiration_date else "Unavailable",
            "domain_expiration_days": domain_expiration_days,
            "url_length": len(url)
        }
    except Exception as e:
        return {
            "url": url,
            "domain_name": "Error",
            "registrar": "Error",
            "creation_date": "Error",
            "expiration_date": "Error",
            "domain_expiration_days": "Error",
            "url_length": len(url)
        }

def mock_model_predict(url_features):
    # Fake logic for demo purposes
    return "Legitimate" if "microsoft" in url_features["url"].lower() else "Phishing"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    input_url = request.form.get("url")
    if not input_url:
        return render_template("index.html", error="Please enter a URL")

    features = extract_url_features(input_url)
    prediction = mock_model_predict(features)
    return render_template("index.html", prediction=prediction, features=features)

if __name__ == "__main__":
    app.run(debug=True)
