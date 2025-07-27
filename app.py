from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours = float(request.form['hours'])
        age = int(request.form['age'])
        internet = 1 if request.form['internet'] == 'yes' else 0

        features = np.array([[hours, age, internet]])
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]

        return render_template('index.html', result=f"Predicted Marks: {prediction:.2f}")

    except Exception as e:
        return render_template('index.html', result="Error in prediction: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
