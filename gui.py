import tkinter as tk
import ttkbootstrap
from tkinter import ttk 
import downloader

def start(url , state):
    downloader.vid_download(url)    
    if state != 0 :
        downloader.write_to_file(url)
        downloader.download_captions(url)


def first_page():
    
    frame = ttk.Frame(app)
    frame.grid(row=0 , column=0 , sticky="nswe")
    app.rowconfigure(0 , weight=1)
    app.columnconfigure(0,weight=1)
    app_name = ttk.Label(frame, text="VidVortex", font=("Helvetica", 40))
    app_name.grid(row=0, column=0, columnspan=2, sticky='n', pady=(80, 0))

    # Configure column weights
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # Ensure that the label is centered horizontally
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)


    url_label = ttk.Label(frame, text='URL : ', font=("Helvetica", 14))
    url_label.grid(row=1, column=0, padx=(200,60), pady=(120, 130), sticky='w')

    url = tk.StringVar()
    url_entry = ttk.Entry(frame, textvariable=url)
    url_entry.grid(row=1, column=0, padx=(300, 0) , pady=(120, 130), sticky='ew')

    state = tk.IntVar()
    config_button = tk.Checkbutton(frame ,height=2 , width=12 ,text='Data' ,variable=state)
    config_button.grid(row=2 , column=0 ,sticky='w' , padx=(590,0))

    start_button = tk.Button(frame ,height=2 , width=12 ,text='Start',command=lambda : start(url.get(), state=state.get()))
    start_button.grid(row=2 , column=0 ,sticky='w' , padx=(300,0) )




app = tk.Tk()
app.geometry("1024x768")
style = ttkbootstrap.Style(theme="vapor")
style.theme_use()
first_page()
app.mainloop()


