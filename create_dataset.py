import pandas as pd
import numpy as np

np.random.seed(42)

# Generate 500 student records with BALANCED dropout distribution (50/50)
n_students = 500
dropout_students = 250  # 250 dropout = 1 (high risk)
non_dropout_students = 250  # 250 non-dropout = 0 (low risk)

data = []

# Generate AT-RISK students (likely to dropout - HIGH RISK)
# Ranges: Attendance 45-87%, Study hours 1-4, Failures 2-4+
for i in range(dropout_students):
    age = np.random.randint(18, 26)
    gender = np.random.randint(0, 2)
    attendance = np.random.randint(45, 88)  # Attendance 45-87%
    study_hours = np.random.randint(1, 5)  # Study hours 1-4
    family_income = np.random.randint(1, 3)  # Low income (1-2)
    internet = np.random.choice([0, 1], p=[0.7, 0.3])  # 70% no internet
    failures = np.random.randint(2, 6)  # Failures 2-5
    health = np.random.randint(1, 4)  # Poor health (1-3)
    motivation = np.random.randint(1, 4)  # Low motivation (1-3)
    dropout = 1
    
    data.append([age, gender, attendance, study_hours, family_income, internet, failures, health, motivation, dropout])

# Generate SUCCESSFUL students (unlikely to dropout - LOW RISK)
# Ranges: Attendance 88-100%, Study hours 5-8, Failures 0
for i in range(non_dropout_students):
    age = np.random.randint(18, 26)
    gender = np.random.randint(0, 2)
    attendance = np.random.randint(88, 101)  # Attendance 88-100%
    study_hours = np.random.randint(5, 9)  # Study hours 5-8
    family_income = np.random.randint(3, 6)  # Higher income (3-5)
    internet = np.random.choice([0, 1], p=[0.1, 0.9])  # 90% have internet
    failures = 0  # Zero failures
    health = np.random.randint(3, 6)  # Good health (3-5)
    motivation = np.random.randint(3, 6)  # High motivation (3-5)
    dropout = 0
    
    data.append([age, gender, attendance, study_hours, family_income, internet, failures, health, motivation, dropout])

# Shuffle the data
np.random.shuffle(data)

# Create DataFrame
df = pd.DataFrame(data, columns=['age', 'gender', 'attendance', 'study_hours', 'family_income', 'internet', 'failures', 'health', 'motivation', 'dropout'])

# Save to CSV
df.to_csv('data/student_data.csv', index=False)

# Print summary
print("✅ Dataset created with 500 students")
print(f"✅ HIGH RISK (Dropout=1): {df['dropout'].sum()} ({df['dropout'].sum()/len(df)*100:.1f}%)")
print(f"✅ LOW RISK (Dropout=0): {len(df[df['dropout']==0])} ({len(df[df['dropout']==0])/len(df)*100:.1f}%)")
print(f"\n📊 Dataset Shape: {df.shape}")
print(f"\n🎯 First 5 rows:")
print(df.head())
print(f"\n📊 Feature Statistics for HIGH RISK students:")
print(df[df['dropout']==1].describe())
print(f"\n📊 Feature Statistics for LOW RISK students:")
print(df[df['dropout']==0].describe())
