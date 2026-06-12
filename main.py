import os
import sys
import threading
import tkinter as tk
from tkinter import messagebox

import yt_dlp

if getattr(sys, "frozen", False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

ffmpeg_path = os.path.join(base_path, "ffmpeg")

if not os.path.exists(ffmpeg_path):
    print("FFmpeg folder not found!")
else:
    print("FFmpeg found:", ffmpeg_path)

window = tk.Tk()
window.title("YouTube Audio Downloader")
window.geometry("800x600")


def progress_hook(d):
    if d["status"] == "downloading":
        progress_label.config(text=f"Progress: {d['_percent_str']}")

    elif d["status"] == "finished":
        progress_label.config(text="Download Complete!")


def get_info():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    try:
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)

        title = info.get("title", "Unknown")
        uploader = info.get("uploader", "Unknown")
        duration = info.get("duration", 0)
        views = info.get("view_count", "Unknown")
        upload_date = info.get("upload_date", "Unknown")
        formats = len(info.get("formats", []))  # type: ignore

        minutes = duration // 60  # type: ignore
        seconds = duration % 60  # type: ignore

        output_box.delete("1.0", tk.END)

        output_box.insert(
            tk.END,
            f"""
========== VIDEO INFO ==========

Title       : {title}
Uploader    : {uploader}
Duration    : {minutes}m {seconds}s
Views       : {views}
Upload Date : {upload_date}
Formats     : {formats}

===============================
""",
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def download_audio():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    ydl_opts = {
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "progress_hooks": [progress_hook],
        "format": "bestaudio",
        "ffmpeg_location": ffmpeg_path,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:  # type: ignore
            ydl.download([url])

        messagebox.showinfo("Success", "Download Complete!")

    except Exception as e:
        messagebox.showerror("Download Failed", str(e))


def start_download():
    threading.Thread(target=download_audio, daemon=True).start()


title_label = tk.Label(
    window,
    text="YouTube Audio Downloader",
    font=("Arial", 20, "bold"),
)
title_label.pack(pady=10)


url_label = tk.Label(window, text="Enter YouTube URL:")
url_label.pack()

url_entry = tk.Entry(window, width=80)
url_entry.pack(pady=5)


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

info_button = tk.Button(
    button_frame,
    text="Get Info",
    width=15,
    command=get_info,
)
info_button.pack(side=tk.LEFT, padx=10)

download_button = tk.Button(
    button_frame,
    text="Download Audio",
    width=15,
    command=start_download,
)
download_button.pack(side=tk.LEFT, padx=10)


progress_label = tk.Label(
    window,
    text="Ready",
    font=("Arial", 12),
)
progress_label.pack(pady=10)


output_box = tk.Text(
    window,
    width=90,
    height=20,
)
output_box.pack(pady=10)


window.mainloop()
