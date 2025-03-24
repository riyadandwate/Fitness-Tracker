from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model
with open("model/calories_predictor.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/")
def home():
    return render_template("index.html")  # This will render your HTML page

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from the form
        data = request.json  # Using JSON data instead of form

        gender = data['Gender']
        age = int(data['Age'])
        height = float(data['Height'])
        weight = float(data['Weight'])
        duration = float(data['Duration'])
        heart_rate = float(data['Heart_Rate'])
        body_temp = float(data['Body_Temp'])

        # Convert data to DataFrame
        input_data = {
            "Gender": [gender],
            "Age": [age],
            "Height": [height],
            "Weight": [weight],
            "Duration": [duration],
            "Heart_Rate": [heart_rate],
            "Body_Temp": [body_temp]
        }
        input_df = pd.DataFrame(input_data)

        # Encode Gender (male = 0, female = 1)
        input_df["Gender"] = input_df["Gender"].map({"male": 0, "female": 1})

        # Make prediction
        prediction = model.predict(input_df)
        calories_burned = round(prediction[0], 2)

        # Return the result in JSON format
        return jsonify({"calories_burned": calories_burned})

    except Exception as e:
        return jsonify({"error": str(e)})

# Daily exercise plan route
@app.route("/exercise_plan")
def exercise_plan():
    plan = {
        "Day 1": "Light Stretching & Mobility (30 minutes)",
        "Day 2": "Walking and Core Work (40 minutes)",
        "Day 3": "Strength Training (Bodyweight) (40 minutes)",
        "Day 4": "Yoga and Flexibility (30 minutes)",
        "Day 5": "Running or Cycling + Full Body (40-45 minutes)",
        "Day 6": "High-Intensity Interval Training (HIIT) (30 minutes)",
        "Day 7": "Active Recovery and Stretching (30 minutes)"
    }
    return jsonify(plan)

if __name__ == "__main__":
    app.run(debug=True)
