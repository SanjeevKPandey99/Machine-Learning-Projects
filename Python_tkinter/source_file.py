import os
import webbrowser
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename


root = Tk()
root.title("Simple_Notepad")
root.geometry("600x400")

file = None


def new_file():
    global file
    file = None
    root.title("Simple_Notepad")
    text_area.delete(1.0, END)

def open_file():
    global file
    file = askopenfilename(defaultextension=".txt", 
                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        with open(file, "r") as f:
            text_area.insert(1.0, f.read())

def save_file():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', 
                                 defaultextension=".txt", 
                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "w") as f:
                f.write(text_area.get(1.0, END))
            root.title(os.path.basename(file) + " - Notepad")
    else:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, END))

def quit_app():
    root.destroy()

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def show_about():
    webbrowser.open("https://support.microsoft.com/en-us/windows/help-in-notepad-4d68c388-2ff2-0e7f-b706-35fb2ab88a8c")


text_area = Text(root, undo=True, wrap="word", font=("Arial", 12))
text_area.pack(fill=BOTH, expand=True)

scrollbar = Scrollbar(text_area)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)


menu_bar = Menu(root)


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)
menu_bar.add_cascade(label="File", menu=file_menu)


edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)


help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="View Help", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)


root.config(menu=menu_bar)


root.mainloop()
