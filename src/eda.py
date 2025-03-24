import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
calories_df = pd.read_csv(r"D:\Fitness Tracker\data\calories.csv")
exercise_df = pd.read_csv(r"D:\Fitness Tracker\data\exercise.csv")


# Display basic information
print(f"Calories Data Shape: {calories_df.shape}")
print(f"Exercise Data Shape: {exercise_df.shape}\n")

print("Calories Data Sample:\n", calories_df.head(), "\n")
print("Exercise Data Sample:\n", exercise_df.head(), "\n")

# Check for missing values
print("\n🔍 Missing Values:")
print(calories_df.isnull().sum())
print(exercise_df.isnull().sum())

# Data types
print("\n🛠 Data Types:")
print(calories_df.dtypes)
print(exercise_df.dtypes)

# Dataset statistics
print("\n📈 Calories Dataset Summary:")
print(calories_df.describe())

print("\n📉 Exercise Dataset Summary:")
print(exercise_df.describe())

# Handle categorical variables (Convert 'Gender' to numeric)
exercise_df["Gender"] = exercise_df["Gender"].map({"male": 0, "female": 1})

# Drop duplicate rows if any
calories_df.drop_duplicates(inplace=True)
exercise_df.drop_duplicates(inplace=True)

# Check correlation after conversion
correlation = exercise_df.corr()
print("\n🔗 Correlation Matrix (Exercise Data):\n", correlation)

# Ensure the `data` directory exists before saving
output_dir = "../data/"
os.makedirs(output_dir, exist_ok=True)

# Save cleaned datasets
calories_df.to_csv(os.path.join(output_dir, "processed_calories.csv"), index=False)
exercise_df.to_csv(os.path.join(output_dir, "processed_exercise.csv"), index=False)

print("\n✅ Processed files saved successfully!")

# ==========================
# 🔹 Data Visualization 🔹
# ==========================

# 1️⃣ Histogram of Calories
plt.figure(figsize=(8, 5))
sns.histplot(calories_df["Calories"], bins=30, kde=True, color='blue')
plt.title("Distribution of Calories")
plt.xlabel("Calories Burned")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("../data/calories_histogram.png")  # Save histogram
plt.show()

# 2️⃣ Boxplot of Exercise Duration
plt.figure(figsize=(8, 5))
sns.boxplot(x=exercise_df["Duration"], color='red')
plt.title("Boxplot of Exercise Duration")
plt.xlabel("Duration (minutes)")
plt.grid(True)
plt.savefig("../data/duration_boxplot.png")  # Save boxplot
plt.show()

# 3️⃣ Heatmap of Correlation
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig("../data/correlation_heatmap.png")  # Save heatmap
plt.show()
