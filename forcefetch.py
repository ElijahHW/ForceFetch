from tkinter import filedialog
import tkinter as tk
import customtkinter as ct
from pytube import YouTube
import time
import subprocess
import getpass
import os
import sys 


#Configs
username = getpass.getuser()

def start_instructions():
    title.configure(text="Fetching Stream")
    link = link_input.get()
    if is_youtube_link(link):
        print("The link is a valid YouTube link.")
        progress_bar.pack(padx=10, pady=10)
        progress_text.pack(padx=10, pady=10)
        progress_text.pack(padx=10, pady=10)
        time.sleep(0.246)
        start_download()
    else:
        title.configure(text="The link is not a valid YouTube link.", text_color="red")
    
def is_youtube_link(link):
    try:
        yt = YouTube(link)
        return True
    except:
        return False

def start_download():
    title.configure(text="Downloading..")
    try: 
        YTLink = link_input.get()
        YTObject = YouTube(YTLink, on_progress_callback=on_progress)
        stream = YTObject.streams.get_highest_resolution()
        title.configure(text=YTObject.title, text_color="white")
        # Download 
        stream.download('C:\\Users\\'+username+'\\Desktop\\ForceFetch\\')
        completeDownload()
    except Exception as e:
        raise e
        actionBtn.configure(text="Try another link")
        finish_label.configure(text="Error while trying to download...", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    title.configure(text="Fetching Streams...")
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    prctg_completion = bytes_downloaded / total_size * 100
    percentage_str = str(int(prctg_completion))
    progress_text.configure(text=percentage_str + '%')
    progress_bar.set(float(prctg_completion) / 100)
    actionBtn.configure(text="Please wait...")
    progress_text.update()

def browse_button():
    subprocess.call("explorer C:\\users\\"+username+"\\Desktop\\ForceFetch\\", shell=True)
    app.destroy()

def completeDownload():
    title.configure(text="Success! ✨")
    actionBtn.configure(text="Browse to file", command=browse_button)
    progress_bar.set(100)
    progress_text.pack_forget()
    progress_bar.pack_forget()
    link_input.pack_forget()

def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# System
ct.set_appearance_mode("Dark")
ct.set_default_color_theme("green")

# Frame
app = ct.CTk()
app.geometry("720x480")
app.title("ForceFetch")
app.iconbitmap(default=resource_path('fetcher.ico'))

# UI stuff
title = ct.CTkLabel(app, text="Insert a Youtube Link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tk.StringVar()
link_input = ct.CTkEntry(app, width=350, height=40, textvariable=url_var)
link_input.pack()

# Progress
progress_text = ct.CTkLabel(app, text="0%")
progress_bar = ct.CTkProgressBar(app, width=400, mode="determinate")
progress_bar.set(0)

# Download Button
actionBtn = ct.CTkButton(app, text="Download", command=start_instructions)
actionBtn.pack(padx=10, pady=10)
# Download Finish Label
finish_label = ct.CTkLabel(app, text="")
finish_label.pack()

# Run App
app.mainloop()