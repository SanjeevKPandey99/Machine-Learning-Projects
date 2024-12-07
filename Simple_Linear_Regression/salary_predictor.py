import tkinter as tk
import joblib
import numpy as np
from tkinter import END

model = joblib.load(r"C:\Users\window10\Desktop\AI CLasses\Project\Simple_Linear_Regression\salary.joblib")

def validate_exp(exp):
    if exp.isdigit(): 
        return True
    return False


def validate():
    exp = ent.get()
    if not validate_exp(exp):
        lb2.config(text = "Invalid Input, Kindly enter a valid Experience.",font=("Poppins",16,"normal"),fg= "red")
    else:
        predictpkg()

def predictpkg():
    exp = float(ent.get())
    exp_arr = np.array(exp)
    new_exp = exp_arr.reshape(-1,1)
    pred_pkg = model.predict(new_exp)[0]
    lb2.config(text = f"Predicted Salary is {int(pred_pkg)} Rupees.",font=("Poppins",16,"normal"),fg="#a4133c")


app = tk.Tk()
app.geometry("600x400")
app.title("Salary Prediction")
app.config(background = "#ffb3c1")
app.iconbitmap(r"C:\Users\window10\Desktop\AI CLasses\Project\Simple_Linear_Regression\icon1.ico")

lb1 = tk.Label(app, text="SALARY PREDICTOR", bg="#a4133c", fg="white", font=("Poppins",20,"bold"))
lb1.pack(ipadx= 600,ipady=6,pady=2)


ent = tk.Entry(app, font=("Poppins", 20))
ent.insert(END, 'Experiecne(Yrs)')
ent.pack(ipadx=2,ipady=4,pady=6)


btn = tk.Button(app, text="Predict Salary", command=lambda: validate(), bg="#c9184a", fg="white", font=("Poppins",18,"bold"))
btn.pack(ipadx=2,ipady=0.5,pady=2)


lb2 = tk.Label(app, text="", font=("Poppins",16,"normal"), bg="#ffb3c1")
lb2.pack(pady=2)

app.mainloop()