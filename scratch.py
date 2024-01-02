from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type", src="en", dest="hi"):  # Update default language codes for English and Hindi
    text1 = text
    src1 = src
    dest1 = dest
    try:
        if text1.strip():  # Check if the text is not empty or contains only whitespace
            trans = Translator()
            trans1 = trans.translate(text1, src=src1, dest=dest1)
            if trans1.text is not None:
                return trans1.text
            else:
                return "Translation Error: Empty response received"
        else:
            return "Translation Error: Input text is empty"
    except Exception as e:
        return f"Translation Error: {str(e)}"




def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("TALK FUSION")
root.geometry("500x700")
root.config(bg="skyblue")

lab_txt = Label(root, text="TALK FUSION", font=("Time New Roman", 40, "bold"))
lab_txt.place(x=50, y=40, height=50, width=400)  # Adjust width to ensure complete text visibility

frame = Frame(root)
frame.place(x=10, y=100, height=450, width=480)

lab_txt = Label(frame, text="Input Text", font=("Time New Roman", 20, "bold"), fg="Red")
lab_txt.place(x=10, y=10)

Sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=40, height=150, width=460)

language = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame, value=language)
comb_sor.place(x=10, y=200, height=40, width=150)
comb_sor.set("English")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=200, height=40, width=100)

comb_dest = ttk.Combobox(frame, value=language)
comb_dest.place(x=320, y=200, height=40, width=150)
comb_dest.set("Hindi")

lab_txt = Label(frame, text="Translated Text", font=("Time New Roman", 20, "bold"), fg="Red")
lab_txt.place(x=10, y=260)

dest_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=290, height=150, width=460)

root.mainloop()
