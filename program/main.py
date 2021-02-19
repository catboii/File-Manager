#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import filedialog 
from mediaplayer import media_player
from tpdf import text_to_pdf
from mergewindow import merge_window
from notepad import note_
from openpdf import open_pdff
from imagetopdf import i_to_pdf
from openimage import open_image
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File",filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 
    label_file_explorer.configure(text="File Opened: "+filename)

class App:
    def __init__(self, root):
        #setting title
        root.title("File manager")
        #setting window size
        width=500
        height=250
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        browse=tk.Button(root)
        browse["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        browse["font"] = ft
        browse["fg"] = "#000000"
        browse["justify"] = "center"
        browse["text"] = "Browse Files"
        browse["relief"] = "raised"
        browse.place(x=10,y=20,width=72,height=30)
        browse["command"] = self.browse_command

        txt_to_pdf=tk.Button(root)
        txt_to_pdf["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        txt_to_pdf["font"] = ft
        txt_to_pdf["fg"] = "#000000"
        txt_to_pdf["justify"] = "center"
        txt_to_pdf["text"] = "Text to pdf"
        txt_to_pdf["relief"] = "raised"
        txt_to_pdf.place(x=10,y=70,width=69,height=30)
        txt_to_pdf["command"] = self.txt_to_pdf_command

        media=tk.Button(root)
        media["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        media["font"] = ft
        media["fg"] = "#000000"
        media["justify"] = "center"
        media["text"] = "Media Player"
        media["relief"] = "raised"
        media.place(x=90,y=20,width=72,height=30)
        media["command"] = self.media_command

        pd_merge=tk.Button(root)
        pd_merge["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        pd_merge["font"] = ft
        pd_merge["fg"] = "#000000"
        pd_merge["justify"] = "center"
        pd_merge["text"] = "Pdf merge"
        pd_merge["relief"] = "raised"
        pd_merge.place(x=170,y=70,width=78,height=30)
        pd_merge["command"] = self.pd_merge_command

        i_to_pdf=tk.Button(root)
        i_to_pdf["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        i_to_pdf["font"] = ft
        i_to_pdf["fg"] = "#000000"
        i_to_pdf["justify"] = "center"
        i_to_pdf["text"] = "Image to pdf"
        i_to_pdf["relief"] = "raised"
        i_to_pdf.place(x=170,y=20,width=78,height=30)
        i_to_pdf["command"] = self.i_to_pdf_command

        note_pad=tk.Button(root)
        note_pad["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        note_pad["font"] = ft
        note_pad["fg"] = "#000000"
        note_pad["justify"] = "center"
        note_pad["text"] = "Notepad"
        note_pad["relief"] = "raised"
        note_pad.place(x=90,y=70,width=71,height=30)
        note_pad["command"] = self.note_pad_command

        exit_button=tk.Button(root)
        exit_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        exit_button["font"] = ft
        exit_button["fg"] = "#000000"
        exit_button["justify"] = "center"
        exit_button["text"] = "EXIT"
        exit_button.place(x=10,y=190,width=166,height=30)
        exit_button["command"] = self.exit_button_command

        o_image=tk.Button(root)
        o_image["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        o_image["font"] = ft
        o_image["fg"] = "#000000"
        o_image["justify"] = "center"
        o_image["text"] = "Open image"
        o_image.place(x=90,y=120,width=71,height=30)
        o_image["command"] = self.o_image_command

        o_pdf=tk.Button(root)
        o_pdf["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        o_pdf["font"] = ft
        o_pdf["fg"] = "#000000"
        o_pdf["justify"] = "center"
        o_pdf["text"] = "Open PDF"
        o_pdf.place(x=10,y=120,width=71,height=30)
        o_pdf["command"] = self.o_pdf_command

        about_us=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        about_us["font"] = ft
        about_us["fg"] = "#333333"
        about_us["justify"] = "center"
        about_us["text"] = "By team Cyan"
        about_us.place(x=370,y=200,width=117,height=30)

    def browse_command(self):
        #print("Browse Files")
        browseFiles()


    def txt_to_pdf_command(self):
        #print("Text to PDF")
        text_to_pdf()


    def media_command(self):
        print("Media Player")
        media_player()


    def pd_merge_command(self):
        #print("Merge PDF")
        merge_window()


    def i_to_pdf_command(self):
        #print("Images to PDF")
        i_to_pdf()


    def note_pad_command(self):
        #print("Notepad")
        note_()


    def exit_button_command(self):
        root.destroy()


    def o_image_command(self):
        #print("Open images")
        open_image()


    def o_pdf_command(self):
        #print("Opens PDF")
        open_pdff()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


# In[ ]:




