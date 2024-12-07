import tkinter as tk
import joblib
import numpy as np

model = joblib.load(r"C:\Users\window10\Desktop\AI CLasses\Project\salary.joblib")

def validate_exp(exp):
    if exp.isdigit(): 
        return True
    return False


def validate():
    exp = ent.get()
    if not validate_exp(exp):
        lb2.config(text = "Invalid Input, Kindly enter a valid Experience.",font=("robert", 14),fg= "red")
    else:
        predictpkg()

def predictpkg():
    exp = float(ent.get())
    exp_arr = np.array(exp)
    new_exp = exp_arr.reshape(-1,1)
    pred_pkg = model.predict(new_exp)[0]
    lb2.config(text = f"Predicted Salary is {int(pred_pkg)} Rupees.",font=("robert", 18), fg = "blue")


app = tk.Tk()
app.geometry("600x400")
app.title("Salary Prediction")
app.config(background = "skyblue")
app.iconbitmap(r"C:\Users\window10\Desktop\AI CLasses\Project\icon1.ico")

lb1 = tk.Label(app, text="Salary Predictor based on Experience(Yrs)", bg="blue", fg="white", font=("robert", 22, "bold"))
lb1.pack(ipadx= 600,ipady=6,pady=2)


ent = tk.Entry(app, font=("robert", 22),)
ent.pack(ipadx=2,ipady=4,pady=6)


btn = tk.Button(app, text="Predict Salary", command=lambda: validate(), bg="blue", fg="white", font=("robert", 20, "bold"))
btn.pack(ipadx=2,ipady=0.5,pady=2)


lb2 = tk.Label(app, text="", font=("robert", 18), bg="skyblue")
lb2.pack(pady=2)

app.mainloop()