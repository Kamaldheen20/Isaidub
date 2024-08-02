import tkinter as tk
import webbrowser

def open_webpage():
    webbrowser.open("https://isaidub8.co/")


root = tk.Tk()
root.title("Basic Web Page Opener")


root.geometry("300x100")


open_button = tk.Button(root, text="go to the isaidub",command=open_webpage)
open_button.pack(pady=20)

root.mainloop()