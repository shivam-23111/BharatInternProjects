#Importing Required Modules And API`s`

import tkinter as tk
from tkinter import ttk
from googletrans import Translator,LANGUAGES

# Creating a window named "Screen"
Screen = tk.Tk()
Screen.title("Language Translator App by Shivam Tiwari (BHARAT INTERN PROJECT)")
Screen.config(bg="AntiqueWhite2")
LanguageChoices =list(LANGUAGES.values())

# Function to translate the text using google`s API
def Translate():
    

    translator = Translator()
    
    translation = translator.translate(input_text.get("1.0",tk.END),dest=OutputLanguageChoiceMenu.get())
    
    output=translation.text
    output_text.delete("1.0",tk.END)
    output_text.insert(tk.END,output)

#frames
main_frame=tk.Frame(Screen,height=250,width=500) 
secondary_frame=tk.Frame(main_frame)    


# Creating Widgets
#Text widget for text input
input_text = tk.Text(main_frame, fg="black", bg="white",font='Arial 10 ',height=5)


input_label=tk.Label(main_frame,text="INPUT TEXT",font='Arial 10 bold')
output_label=tk.Label(main_frame,text="OUTPUT TEXT LANGUAGE",font='Arial 10 bold')

#Text widget for output text
output_text = tk.Text(main_frame, fg="black", bg="white",font='Arial 10 ',height=5)

#Button widget for calling Translate funtion 
Btn_translate = tk.Button(secondary_frame,text="Translate",command=Translate, bg="AntiqueWhite4", fg="white",width=10)

label=tk.Label(Screen,text="AI LANGUAGE TRANSLATOR APP  (~~BHARAT INTERN~~)")

#Combobox widget for selecting destination language
OutputLanguageChoiceMenu = ttk.Combobox(main_frame,values=LanguageChoices)

# Setting initial value for OutputLanguageChoiceMenu
OutputLanguageChoiceMenu.set('Spanish')


# Placing the widgets to their masters with pack()
main_frame.pack(pady=100)
OutputLanguageChoiceMenu.pack(side=tk.BOTTOM,pady=5)
label.pack()
input_label.pack(side=tk.TOP)
output_label.pack(side=tk.BOTTOM)
input_text.pack( padx=5,pady=50, side=tk.TOP)
secondary_frame.pack()
output_text.pack( padx=5,pady=50, side=tk.BOTTOM)
Btn_translate.pack(side=tk.BOTTOM)

# starting the main window loop
Screen.mainloop()