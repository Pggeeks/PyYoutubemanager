from pytube import YouTube
from pathlib import Path
import re
class YTdownload:
    PATH = Path(__file__).parent.absolute() #gets the path of parent directory 
# can also pass your own path as Path=
    def __init__(self, link, Path=PATH):
        self.Path = Path
        self.link = link

    def Download(self):
        try:
            Yt = YouTube(self.link)
        except Exception:
            print("Connection Error")
        try:
            print(Yt.title)
            video = Yt.streams.filter(file_extension='mp4').get_highest_resolution()
            # remove all the emoji and spaces , symbols
            videopath = video.download(output_path=self.Path, filename=re.sub('[^A-Za-z0-9]+', '_', f'{Yt.title}mp4'))
            return videopath
        except Exception:
            print("Some Error!")
            return None
