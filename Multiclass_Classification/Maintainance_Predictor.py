import tkinter as tk
import joblib
import numpy as np
from tkinter import END

# Load the trained model
model = joblib.load(r"C:\Users\window10\Desktop\AI CLasses\Project\Multiclass_Classification\Maintainance_Predictor.joblib")
scaler = joblib.load(r"C:\Users\window10\Desktop\AI CLasses\Project\Multiclass_Classification\scaler.joblib")

# Function to validate input
def validate_input(input_str):
    try:
        input_list = [float(x) for x in input_str.split(",")]
        if len(input_list) == 7:  # Expecting 7 inputs
            return True
        return False
    except ValueError:
        return False

# Function to validate and predict
def validate_and_predict():
    input_str = ent.get()
    if not validate_input(input_str):
        lb2.config(
            text="Invalid Input! Enter 7 comma-separated numeric values.",
            font=("Poppins", 14, "normal"),
            fg="red"
        )
    else:
        predict_failure(input_str)

# Function to predict output
def predict_failure(input_str):
    input_list = [float(x) for x in input_str.split(",")]
    input_array = np.array(input_list).reshape(1, -1)  # Reshape for model input
    input_array = scaler.transform(input_array)
    print(input_array)
    predicted_failure = model.predict(input_array)[0]
    if predicted_failure == 0:
        lb2.config(
            text=f"Predicted Failure Type: {"Heat Dissipation Failure"}",
            font=("Poppins", 16, "bold"),
            fg="#28a745"
        )
    if predicted_failure == 1:
        lb2.config(
            text=f"Predicted Failure Type: {"No Failure "}",
            font=("Poppins", 16, "bold"),
            fg="#28a745"
        )
    if predicted_failure == 2:
        lb2.config(
            text=f"Predicted Failure Type: {"Overstrain Failure"}",
            font=("Poppins", 16, "bold"),
            fg="#28a745"
        )
    if predicted_failure == 3:
        lb2.config(
            text=f"Predicted Failure Type: {"Power Failure"}",
            font=("Poppins", 16, "bold"),
            fg="#28a745"
        )
    if predicted_failure == 4:
        lb2.config(
            text=f"Predicted Failure Type: {"Random Failures"}",
            font=("Poppins", 16, "bold"),
            fg="#28a745"
        )
    if predicted_failure == 5:
        lb2.config(
            text=f"Predicted Failure Type: {"Tool Wear Failure"}",
            font=("Poppins", 16, "bold"),
            fg="#28a745"
        )
    

# Create the GUI application
app = tk.Tk()
app.geometry("800x400")
app.title("Predictive Maintenance Failure Predictor")
app.config(background="#C4DAD2")  

# Title label
lb1 = tk.Label(
    app,
    text="PREDICTIVE MAINTENANCE FAILURE PREDICTOR",
    bg="#16423C",  
    fg="white",
    font=("Poppins", 20, "bold")
)
lb1.pack(ipadx=600, ipady=6, pady=2)

# Entry for input
ent = tk.Entry(app, font=("Poppins", 16), width=60)
ent.insert(END, 'Enter 7 values, comma-separated (e.g., 1,2,300,310,1500,50,100)')
ent.pack(ipadx=2, ipady=4, pady=6)

# Predict button
btn = tk.Button(
    app,
    text="Predict Failure",
    command=validate_and_predict,
    bg="#6A9C89",  
    fg="white",
    font=("Poppins", 16, "bold")
)
btn.pack(ipadx=2, ipady=0.5, pady=10)

# Label to display prediction result or error
lb2 = tk.Label(app, text="", font=("Poppins", 16, "normal"), bg="#C4DAD2")
lb2.pack(pady=10)

app.mainloop()
