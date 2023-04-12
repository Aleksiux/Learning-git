from pytube import YouTube
import webbrowser
from tkinter import filedialog


def Browse():
    download_directory = filedialog.askdirectory(title="Save Video")
    return download_directory


def Download(url):
    browse = Browse()
    yt = YouTube(url)
    yt = yt.streams.get_highest_resolution()
    try:
        if browse != "":
            yt.download(output_path=browse)
    except:
        webbrowser.open('https://www.youtube.com/watch?v=t3otBjVZzT0')
