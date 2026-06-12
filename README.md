# YouTube Audio Downloader

A desktop YouTube audio downloader built with Python, Tkinter, yt-dlp and FFmpeg.

## Features

* Get video information
* Download best quality audio
* Automatic MP3 conversion
* Download progress display
* Simple GUI interface
* Windows executable support

## Technologies Used

* Python
* Tkinter
* yt-dlp
* FFmpeg
* PyInstaller

## How To Run

Install dependencies:

pip install yt-dlp

Run:

python main.py

## Build EXE

pyinstaller --onefile --windowed main.py

## Controls

1. Enter YouTube URL
2. Click Get Info
3. Click Download Audio

Audio files are saved inside the downloads folder.
