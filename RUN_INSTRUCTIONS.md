# 🚀 RUN GUIDE - TANGLISH EXPLANATION

## 📊 ERRORS FIXED:

✅ **requirements.txt** - Added Flask, pandas, sklearn, joblib
✅ **app.py** - Updated to use trained ML model with joblib
✅ **script.js** - Added form validation code
✅ **train_model.py** - Already working fine
✅ **Dataset** - No issues found

---

## 🎯 STEP-BY-STEP RUN INSTRUCTIONS

### **STEP 1: Virtual Environment Activate Pannu**
```
Windows PowerShell:
& d:\Student_Dropout_Prediction\.venv\Scripts\Activate.ps1

(Athuku apdiye terminal prompt change aaidhi => (.venv) visible aindu)
```

---

### **STEP 2: Dependencies Install Pannu**
```
Command:
pip install -r requirements.txt

Result:
- Flask ..... installed
- pandas .... installed
- scikit-learn ... installed
- joblib .... installed
```

---

### **STEP 3: Model Train Pannu (If not already trained)**
```
Command:
python train_model.py

Output paakanum:
- Dataset loaded
- Model training success
- Accuracy value visible
- "Model saved successfully!" message
```

---

### **STEP 4: Flask Application Run Pannu**
```
Command:
python app.py

Output paakanum:
* Running on http://127.0.0.1:5000
* Debug mode: ON
```

---

### **STEP 5: Browser Open Pannu**
```
Go to: http://localhost:5000

Innum paakanum:
- Home page with form visible
- Predict button clickable
- Results page showing dropout risk
```

---

## 🔍 HOW IT WORKS NOW:

### **TRAIN_MODEL.py:**
```
1. CSV file read pannu (data/student_data.csv)
2. Features separate pannu (age, attendance, failures, etc.)
3. Target separate pannu (dropout = 0 or 1)
4. 80-20 split pannu (train-test)
5. RandomForest model train pannu
6. Model accuracy print pannu
7. models/dropout_model.pkl file save pannu
```

### **APP.py:**
```
1. Startup time: Model load pannu (joblib se)
2. User form fill pannu
3. Submit button click pannu
4. 9 input values collect pannu:
   - age, gender, attendance, study_hours
   - family_income, internet, failures, health, motivation
5. Model.predict() use pannu
6. Probability calculate pannu
7. Result page show pannu (DROPOUT RISK %)
```

### **SCRIPT.js:**
```
1. Form validation pannu
2. Empty fields check pannu
3. Border color change pannu (red/green)
4. Value ranges validate pannu
5. Alert show pannu (if invalid)
```

---

## ⚠️ COMMON ERRORS & FIXES:

### Error #1: "ModuleNotFoundError: No module named 'flask'"
**Reason:** Dependencies install na pannalai
**Fix:** Step 2 execute pannu (pip install -r requirements.txt)

### Error #2: "Model file not found!"
**Reason:** Model train na pannalai
**Fix:** Step 3 execute pannu (python train_model.py)

### Error #3: "Address already in use"
**Reason:** Flask already running
**Fix:** Terminal close pannu, new terminal open pannu, restart pannu

### Error #4: "KeyError: 'dropout'"
**Reason:** Dataset CSV wrong column name
**Fix:** CSV file check pannu, correct column name use pannu

---

## ✨ FEATURES WORKING NOW:

✅ Form validation - Real-time feedback
✅ ML predictions - Trained model use pannu
✅ Probability calculation - Dropout % show pannu
✅ Error handling - Try-except safe
✅ Model persistence - joblib save/load

---

## 📝 TOTAL COMMANDS SUMMARY:

```powershell
# 1. Virtual environment activate
& d:\Student_Dropout_Prediction\.venv\Scripts\Activate.ps1

# 2. Dependencies install
pip install -r requirements.txt

# 3. Model training (if needed)
python train_model.py

# 4. Flask server run
python app.py

# 5. Browser open
http://localhost:5000
```

---

## 🎉 DONE! ALL FIXED & READY TO RUN!

Sema! Ellame aaidhu! Now machine learning prediction correct ah work pannidhu!
