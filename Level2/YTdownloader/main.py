from pytube import YouTube
import webbrowser
from time import sleep


def Download(url):
    yt = YouTube(url)
    yt = yt.streams.get_audio_only()
    try:
        yt.download()
    except:
        print("Something went wrong.")
        sleep(3)
        webbrowser.open('https://www.youtube.com/watch?v=t3otBjVZzT0')


Download('https://www.youtube.com/watch?v=Jw3tIMZ2ilc')
