import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load the trained model when the Flask app starts
with open("models/calories_predictor.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Define prediction function
def predict_calories(input_df):
    """ Predicts calories based on user input DataFrame. """
    # Gender encoding: Male -> 0, Female -> 1
    input_df["Gender"] = input_df["Gender"].map({"male": 0, "female": 1})
    prediction = model.predict(input_df)
    return round(prediction[0], 2)  # Return rounded value

# Home route to check if the API is working
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running. Use POST /predict to make predictions."})

# Prediction route to handle POST requests
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from the request (JSON)
        data = request.get_json()
        
        # Ensure all required fields are provided
        required_fields = ["Gender", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Convert input data into a DataFrame
        input_data = {
            "Gender": [data["Gender"]],
            "Age": [data["Age"]],
            "Height": [data["Height"]],
            "Weight": [data["Weight"]],
            "Duration": [data["Duration"]],
            "Heart_Rate": [data["Heart_Rate"]],
            "Body_Temp": [data["Body_Temp"]]
        }
        input_df = pd.DataFrame(input_data)

        # Predict calories burned
        calories_burned = predict_calories(input_df)
        
        # Return the prediction as JSON response
        return jsonify({"prediction": calories_burned})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
