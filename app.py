import pandas as pd
import lightgbm as lgb
import pickle 

from flask import Flask, jsonify, request, render_template_string

# Load the model
#model = cb.CatBoostClassifier()
#model.load_model("loan_catboost_model.cbm")

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Init the app
app = Flask("default")

def determine_age_group(age):
    if age <= 1:
        return 'Infants'
    elif age <= 12:
        return 'Children'
    elif age <= 18:
        return 'Adolescents'
    elif age <= 33:
        return 'Young Adults'
    elif age <= 44:
        return 'Adults 34-44'
    elif age <= 54:
        return 'Adults 45-54'
    elif age <= 64:
        return 'Adults 55-64'
    elif age <= 74:
        return 'Seniors 65-74'
    else:
        return 'Seniors 75+'

def determine_bmi_category(bmi, age):
    if age <= 19:
        return 'Younger than 20'
    elif bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        return 'Normal weight'
    elif 25.0 <= bmi <= 29.9:
        return 'Pre-obesity'
    elif 30.0 <= bmi <= 34.9:
        return 'Obesity class I'
    elif 35.0 <= bmi <= 39.9:
        return 'Obesity class II'
    else:
        return 'Obesity class III'

@app.route("/", methods=["GET"])
def form():
    # HTML form for user input
    return render_template_string('''
    <html>
    <body>
        <form action="/predict" method="post">
            Gender: <select name="gender">
                <option value="Female">Female</option>
                <option value="Male">Male</option>
            </select><br>
            Age: <input type="number" name="age"><br>
            Hypertension: <input type="checkbox" name="hypertension" value="1"><br>
            Heart Disease: <input type="checkbox" name="heart_disease" value="1"><br>
            Ever Married: <select name="ever_married">
                <option value="Yes">Yes</option>
                <option value="No">No</option>
            </select><br>
            Work Type: <select name="work_type">
                <option value="Private">Private</option>
                <option value="Self-employed">Self-employed</option>
                <option value="Govt_job">Govt Job</option>
                <option value="Children">Children</option>
            </select><br>
            Residence Type: <select name="Residence_type">
                <option value="Urban">Urban</option>
                <option value="Rural">Rural</option>
            </select><br>
            Avg Glucose Level: <input type="text" name="avg_glucose_level"><br>
            BMI: <input type="text" name="bmi"><br>
            Smoking Status: <select name="smoking_status">
                <option value="Never smoked">Never smoked</option>
                <option value="Formerly smoked">Formerly smoked</option>
                <option value="Smokes">Smokes</option>
            </select><br>
            <input type="submit">
        </form>
    </body>
    </html>
    ''')

@app.route("/predict", methods=["POST"])
def predict():
    # Get the provided form data
    data = request.form.to_dict()
    data['hypertension'] = 1 if 'hypertension' in data else 0
    data['heart_disease'] = 1 if 'heart_disease' in data else 0
    # Convert data types as needed
    data['age'] = int(data['age'])
    data['avg_glucose_level'] = float(data['avg_glucose_level'])
    data['bmi'] = float(data['bmi'])
    
    # Automatically determine age group and BMI category
    data['age_group'] = determine_age_group(data['age'])
    data['bmi_category'] = determine_bmi_category(data['bmi'], data['age'])
    
    # Perform a prediction
    preds = model.predict_proba(pd.DataFrame([data]))[0, 1]
    # Output json with prediction
    return jsonify({"default_proba": preds})

if __name__ == "__main__":
    # Run the app on local host and port 8989
    app.run(debug=True, host="0.0.0.0", port=8989)