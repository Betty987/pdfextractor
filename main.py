import tkinter as tk
from PIL import Image,ImageTk
import PyPDF2
from tkinter.filedialog import askopenfile
import customtkinter

#initializing the app
root = tk.Tk()

canvas = tk.Canvas(root,width=500,height=300)
canvas.grid(columnspan=3,rowspan=3)

#logo
logo = Image.open("logo.png")
logo = logo.resize((270, 165), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)#convert it to a tkinter image
logo_label=tk.Label(image=logo) #make it a widget
logo_label.image = logo #
logo_label.grid(column=1,row=0)


#instructions
instructions = tk.Label(root,text="Select a PDF file to extract",font = "Raleway")
instructions.grid(columnspan=3,column=0,row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root,mode='rb',title="Choose a file",filetypes=[("Pdf file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content=page.extractText()
        print(page_content)

        #text_box
        text_box = tk.Text(root,height=10,width=50,padx=15,pady=15)
        text_box.insert(1.0,page_content)
        text_box.tag_configure("center",justify="center")
        text_box.tag_add("center",1.0,"end")
        text_box.grid(column=1,row=3)

        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_btn = customtkinter.CTkButton(root,text ="Browse",bg_color="black",fg_color="blue",height=28,width=140,command=lambda:open_file())
browse_text.set("Browse")
browse_btn.grid(column=1,row=2)

canvas = tk.Canvas(root,width=500,height=300)
canvas.grid(columnspan=3,rowspan=3)

#running the app

root.mainloop()
