import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib
import os

# Load dataset
print("📊 Loading dataset...")
data = pd.read_csv("data/student_data.csv")

print(f"✅ Dataset loaded: {data.shape[0]} students, {data.shape[1]} features")
print(f"✅ Dropout cases: {data['dropout'].sum()} ({data['dropout'].sum()/len(data)*100:.1f}%)")

# Features & target
X = data.drop("dropout", axis=1)
y = data["dropout"]

# Normalize features for better model performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# Split data (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\n📚 Training set: {len(X_train)} students")
print(f"📚 Testing set: {len(X_test)} students")

# Train RandomForest Model
print("\n🤖 Training Random Forest Model...")
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

# Evaluation Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\n📈 Model Performance Metrics:")
print(f"✅ Accuracy:  {accuracy*100:.2f}%")
print(f"✅ Precision: {precision*100:.2f}%")
print(f"✅ Recall:    {recall*100:.2f}%")
print(f"✅ F1-Score:  {f1*100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(f"\n📊 Confusion Matrix:")
print(f"✅ True Negatives:  {cm[0][0]}")
print(f"✅ False Positives: {cm[0][1]}")
print(f"✅ False Negatives: {cm[1][0]}")
print(f"✅ True Positives:  {cm[1][1]}")

# Feature Importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\n🎯 Feature Importance:")
print(feature_importance)

# Save model and scaler
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/dropout_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(X.columns, "models/feature_columns.pkl")

print("\n✅ Model saved successfully!")
print("✅ Scaler saved successfully!")
print("✅ Feature columns saved successfully!")

