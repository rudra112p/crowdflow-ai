import joblib
import pandas as pd

# Load trained CrowdFlow AI model
model = joblib.load("models/random_forest_model.pkl")

# Example journey segment
test_data = pd.DataFrame([{
    "From Station": "Oxford Circus",
    "To Station": "Piccadilly Circus",
    "Line": "Bakerloo",
    "Dir": "SB",
    "Day_Type": "Monday",
    "Time_Slot": "0830-0845"
}])

prediction = model.predict(test_data)

print("CrowdFlow AI Test Prediction")
print("----------------------------")
print("From: Oxford Circus")
print("To: Piccadilly Circus")
print("Line: Bakerloo")
print("Day: Monday")
print("Time: 08:30")
print(f"Predicted Passenger Load: {prediction[0]:.2f}")