import customtkinter
from tkinter import *
from tkinter import ttk
import os
import check_file
app = Tk()

def download_file():
    check_file.git_repo(search_box.get())

app.geometry("450x450")
app.title("Git Hub Loader")
customtkinter.set_default_color_theme("green")
app.configure(background="#2B2B2B")

#git hub search box
url_var = StringVar()
ui_title = customtkinter.CTkLabel(app,text="Enter your Git Hub Link",text_color="#9090EE",font=("Terminal",20))
ui_title.pack()
search_box = customtkinter.CTkEntry(app,width=300,height=30,textvariable=url_var)
search_box.pack()
#file box
file_var=StringVar()
ui_file = customtkinter.CTkLabel(app,text="Enter your Main File Name",text_color="#DBDB70",font=("Terminal",20))
ui_file.pack(padx=10,pady=10)
file_box = customtkinter.CTkEntry(app,width=300,height=30,textvariable=file_var)
file_box.pack()
#button

def generate_file():

    download_file()
    check_file.find_files(file_box.get())
    #progressbar.destroy()
    finish_label=customtkinter.CTkLabel(app,text="Finished",font=("Terminal",20),text_color='white')
    finish_label.pack()

# progressbar = ttk.Progressbar(mode="indeterminate")
# progressbar.start()

# temp_label = customtkinter.CTkLabel(app,text="")
# temp_label.configure(text=progressbar.pack())
# temp_label.pack()
ui_button = customtkinter.CTkButton(app,text="Generate File",command=generate_file)
ui_button.pack(padx=10,pady=10)


app.mainloop()
