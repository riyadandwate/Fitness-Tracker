import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ✅ Load datasets
exercise_df = pd.read_csv("data/exercise.csv")
calories_df = pd.read_csv("data/calories.csv")

# ✅ Merge datasets on "User_ID"
df = pd.merge(exercise_df, calories_df, on="User_ID")

# ✅ Encode categorical variable (Gender: Male → 0, Female → 1)
df["Gender"] = df["Gender"].map({"male": 0, "female": 1})

# ✅ Define features (X) and target variable (y)
X = df.drop(columns=["User_ID", "Calories"])  # Features
y = df["Calories"]  # Target variable

# ✅ Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ Save the trained model
with open("model/calories_predictor.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("✅ Model training completed & saved as 'calories_predictor.pkl'")
