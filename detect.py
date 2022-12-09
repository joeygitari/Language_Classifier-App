# Language classifier with interface

from tkinter import *

from langdetect import detect
from langdetect import detect_langs
from languages import all_languages_codes

root = Tk()
root.title("Language Classifier")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(background="black")

def detect_now():
    text_=text1.get(1.0, END)
    language_code = detect(text_)   

    sentence = all_languages_codes.get(language_code),language_code
    text2.delete(1.0, END)
    text2.insert(END, sentence) # type: ignore    

label1 = Label(root, text = "Enter text in any language ", font = "times 20 bold italic", bg = "black", width = 20, bd = 5, relief = GROOVE)
label1.place(x = 100, y = 50)

label2 = Label(root, text = "Result of classification ", font = "times 20 bold italic", bg = "black", width = 20, bd = 5, relief = GROOVE)
label2.place(x = 720, y = 50)

#first frame
f = Frame(root, bg="black", bd = 5)
f.place(x = 10, y = 118, width = 440, height = 210)

text1 = Text(f, font = "Times 18", bg = "black", relief = GROOVE, wrap = WORD)
text1.place(x = 0, y= 0, width = 430, height = 200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side = "right", fill = 'y')

scrollbar1.configure(command = text1.yview)
text1.configure(yscrollcommand = scrollbar1.set)

#second frame
f1 = Frame(root, bg="black", bd = 5)
f1.place(x = 620, y = 118, width = 440, height = 210)

text2 = Text(f1, font = "Times 18", bg = "black", relief = GROOVE, wrap = WORD)
text2.place(x = 0, y= 0, width = 430, height = 200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side = "right", fill = 'y')

scrollbar2.configure(command = text2.yview)
text2.configure(yscrollcommand = scrollbar2.set)

#translate button
detect_lang = Button(root, text = "Classify", font = ("Times", 20, "bold", "italic"), activebackground = "black", cursor = "hand2",
                   bd = 1, width = 10, height = 2, bg = "black", fg = "black", command = detect_now)

detect_lang.place(x = 476, y = 250)


root.mainloop()