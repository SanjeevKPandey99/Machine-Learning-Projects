import tkinter as tk
import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load(r"C:\Users\window10\Desktop\AI CLasses\Project\Multilinear_Regression\Student_Performance.joblib")
scaler = joblib.load(r"C:\Users\window10\Desktop\AI CLasses\Project\Multilinear_Regression\scaler.joblib")

def validate_inputs(inputs):
    """Validate that all inputs are numeric."""
    try:
        return all(float(value) for value in inputs)
    except ValueError:
        return False

def predict_performance():
    """Predict the target variable using the model."""
    inputs = [entry_hours.get(), entry_scores.get(), entry_sleep.get(), entry_papers.get()]
    if not validate_inputs(inputs):
        lb_result.config(text="Invalid Input. Enter numeric values for all fields.", font=("Helvetica", 14), fg="red")
        return

    # Prepare inputs for prediction
    features = np.array([float(value) for value in inputs]).reshape(1, -1)
    features = scaler.transform(features)


    prediction = model.predict(features)[0]


    # Display result
    lb_result.config(text=f"Predicted Performance Index: {round(prediction)}", font=("Helvetica", 18), fg="darkgreen")

app = tk.Tk()
app.geometry("800x500")
app.title("Student Performance Predictor")
app.config(background="#f2f2f2")  



lb_title = tk.Label(app, text="Student Performance Predictor", bg="#4682B4", fg="white", font=("Helvetica", 22, "bold"))
lb_title.pack(ipadx=800, ipady=6, pady=2)

frame_inputs = tk.Frame(app, bg="#f2f2f2")
frame_inputs.pack(pady=10)


tk.Label(frame_inputs, text="Hours Studied:", bg="#f2f2f2", font=("Helvetica", 16)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_hours = tk.Entry(frame_inputs, font=("Helvetica", 16), bg="#ffffff", fg="#000000")
entry_hours.grid(row=0, column=1, padx=10, pady=5)


tk.Label(frame_inputs, text="Previous Scores:", bg="#f2f2f2", font=("Helvetica", 16)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_scores = tk.Entry(frame_inputs, font=("Helvetica", 16), bg="#ffffff", fg="#000000")
entry_scores.grid(row=1, column=1, padx=10, pady=5)


tk.Label(frame_inputs, text="Sleep Hours:", bg="#f2f2f2", font=("Helvetica", 16)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_sleep = tk.Entry(frame_inputs, font=("Helvetica", 16), bg="#ffffff", fg="#000000")
entry_sleep.grid(row=2, column=1, padx=10, pady=5)


tk.Label(frame_inputs, text="Sample Papers Practiced:", bg="#f2f2f2", font=("Helvetica", 16)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_papers = tk.Entry(frame_inputs, font=("Helvetica", 16), bg="#ffffff", fg="#000000")
entry_papers.grid(row=3, column=1, padx=10, pady=5)


btn_predict = tk.Button(app, text="Predict Performance Index", command=predict_performance, bg="#4682B4", fg="white", font=("Helvetica", 16, "bold"))
btn_predict.pack(ipadx=10, ipady=5, pady=20)


lb_result = tk.Label(app, text="", font=("Helvetica", 18), bg="#f2f2f2")
lb_result.pack(pady=10)


app.mainloop()
