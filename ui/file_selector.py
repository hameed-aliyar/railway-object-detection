import tkinter as tk
from tkinter import filedialog

def get_video_path():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(
        title="Select video",
        filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
    )
    return path
