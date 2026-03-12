from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load trained model, scaler, and feature columns
model_path = "models/dropout_model.pkl"
scaler_path = "models/scaler.pkl"
features_path = "models/feature_columns.pkl"

if os.path.exists(model_path) and os.path.exists(scaler_path):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    feature_columns = joblib.load(features_path)
    print("✅ Model, scaler, and features loaded successfully!")
else:
    print("❌ ERROR: Model files not found! Run create_dataset.py and train_model.py first")
    model = None
    scaler = None
    feature_columns = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # GET request - show the form
    if request.method == 'GET':
        return render_template('predict.html')
    
    # POST request - process the form
    try:
        # Get input values from form
        age = int(request.form.get('age', 20))
        gender = int(request.form.get('gender', 0))
        attendance = int(request.form.get('attendance', 75))
        study_hours = int(request.form.get('study_hours', 2))
        family_income = int(request.form.get('family_income', 2))
        internet = int(request.form.get('internet', 1))
        failures = int(request.form.get('failures', 0))
        health = int(request.form.get('health', 3))
        motivation = int(request.form.get('motivation', 3))

        # Determine gender strings for display
        gender_word = 'Male' if gender == 1 else 'Female'
        gender_pronoun = 'he' if gender == 1 else 'she'
        gender_pronoun_cap = gender_pronoun.capitalize()

        # Prepare input array in correct order (same as training data)
        input_data = np.array([[age, gender, attendance, study_hours, family_income, 
                               internet, failures, health, motivation]])
        
        # Convert to DataFrame with correct column names
        input_df = pd.DataFrame(input_data, columns=feature_columns)

        # Get prediction from trained model
        if model is not None and scaler is not None:
            # Normalize input using the scaler
            input_scaled = scaler.transform(input_df)
            
            # Make prediction
            prediction = model.predict(input_scaled)[0]
            probability = model.predict_proba(input_scaled)[0]
            
            # Generate result message based on prediction and probability
            if prediction == 1:  # High risk (dropout = 1)
                risk_percentage = probability[1] * 100
                result = f"⚠️ HIGH Dropout Risk ({risk_percentage:.1f}% Probability)"
                risk_level = "HIGH"
            else:  # Low risk (dropout = 0)
                risk_percentage = probability[0] * 100
                result = f"✅ LOW Dropout Risk ({risk_percentage:.1f}% Probability)"
                risk_level = "LOW"
            
            # Store for result page
            prediction_detail = {
                'result': result,
                'risk_level': risk_level,
                'probability': risk_percentage,
                'low_prob': probability[0] * 100,
                'high_prob': probability[1] * 100
            }
        else:
            result = "❌ ERROR: Model not loaded. Please train the model first."
            prediction_detail = {'result': result, 'risk_level': 'ERROR', 'probability': 0}

    except Exception as e:
        result = f"❌ ERROR: {str(e)}"
        prediction_detail = {'result': result, 'risk_level': 'ERROR', 'probability': 0}

    # pass gender info to template as well
    return render_template(
        'result.html', 
        prediction=result,
        gender_word=gender_word,
        pronoun_cap=gender_pronoun_cap
    )

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
