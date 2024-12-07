import tkinter as tk
from tkinter import ttk
from googletrans import LANGUAGES,Translator
from tkinter import END
from langdetect import detect


def translator():
    detection = detect(f1combobox.get())
    det_name = LANGUAGES.get(detection,"Language not found")
    f1combobox.set(det_name)
    print(f1combobox.set(det_name))
    translation = Translator()
    result_txt = translation.translate(text= text_area1.get(1.0,END),src = f1combobox.get(),dest= f2combobox.get() )
    text_area2.delete(1.0,END)
    text_area2.insert(END,result_txt.text)

app = tk.Tk()
app.geometry("950x600+450+80")
app.title("Translation Tool")

app.config(background= "#e9e9f2")

label1 = tk.Label(app,text="Language Translator",font=("Helvetica", 20, "bold"))
label1.pack(fill="x")

# list = ["English","Hindi","Punjabi","Urdu","Bengali"]

frame = tk.Frame(app)
frame.pack(side="top")
# Frame 1
labelf1 =   tk.LabelFrame(frame,text="Input Label")
labelf1.pack(side="left",expand=True)
f1label = tk.Label(labelf1,text="Input Language")
f1label.pack()
f1combobox = ttk.Combobox(labelf1,values= list(LANGUAGES.values()),state="readonly")
f1combobox.set("Select Language")
f1combobox.pack()
text_area1 = tk.Text(labelf1,height=25,width=60)
text_area1.pack()

# Frame 2
labelf2 = tk.LabelFrame(frame,text= "Output Label")
labelf2.pack(side="right",expand=True)
f2label = tk.Label(labelf2,text="Output Language")
f2label.pack()
f2combobox = ttk.Combobox(labelf2,values= list(LANGUAGES.values()),state="readonly")
f2combobox.set("Select Language")
f2combobox.pack()
text_area2 = tk.Text(labelf2,height=25,width=60)
text_area2.pack()

Button1 = tk.Button(app,text="Translate",font=("Helvetica", 20, "bold"),command=translator)
Button1.pack(side="top",pady=10)

app.mainloop()
