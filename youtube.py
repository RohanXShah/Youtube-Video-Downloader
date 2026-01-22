from tkinter import *
from tkinter import messagebox
import yt_dlp as youtube_dl
        

gui = Tk()
gui.geometry("1980x1080")
gui.configure(bg = "Cyan")
gui.title("Youtube Videos Downlaoder")

lab1 = Label(gui, text='Enter Youtube Video Url')
lab1.place(x = 700, y = 0, height=30, width=200)

entry1 = Entry(gui)
entry1.place(x = 700, y = 60, height=30, width=200)
def clicked():
    messagebox.showinfo("You clicked")

def notification():
    try:
        url = entry1.get()
        ydl_opts = {
            "format": "best", 
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url]) 
    
        messagebox.showinfo("Success")
    except:
        messagebox.showerror("Error")

but = Button(gui, text="Download" ,command = notification)
but.place(x =740, y = 120, height=30, width=100)

gui.mainloop()