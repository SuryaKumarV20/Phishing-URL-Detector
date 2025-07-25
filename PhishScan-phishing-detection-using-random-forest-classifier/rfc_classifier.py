# rfc_classifier.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('uci_dataset.csv')  # ✅ Correct filename



# Drop the 'id' column if it's not a useful feature
df = df.drop(columns=['id'])

# Split features and target
X = df.drop(columns=df.columns[-1])  # all columns except the last
y = df[df.columns[-1]]               # last column as label

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model if needed
# import joblib
# joblib.dump(model, 'rfc_model.pkl')
