# Student Performance Predictor

A Flask-based web app that predicts student marks based on:
- Study hours per day
- Age
- Internet access (yes/no)

Live Demo: https://student-performance-predictor-4zui.onrender.com/

Dataset: Custom CSV with 200+ records

## Machine Learning
- Preprocessing: StandardScaler
- Model: Linear Regression (scikit-learn)
-  Performance:
  - R² Score: 0.94
  - MAE: ~0.94
  - RMSE: ~1.13

## Technologies Used
- Python
- Flask
- HTML/CSS (Jinja2 templating)
- scikit-learn, Pandas, NumPy
- Render (hosting)

## How to Run Locally

```bash
git clone https://github.com/ManavPruthi/student-performance-predictor.git
cd student-performance-predictor
pip install -r requirements.txt
python app.py
