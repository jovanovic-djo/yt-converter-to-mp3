import os
import yt_dlp

# If you create data.py file
from data import URLS, PLAYLISTS


"""
# Other solution is to uncomment this section and fill up array variables with hrefs instead of creating data.py file
URLS = [

]

PLAYLISTS = [

]

"""

def main():
    os.makedirs("converted", exist_ok=True)
    
    video_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'converted/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'noplaylist': True,
    }
    
    playlist_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'converted/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'noplaylist': False,
    }
    
    with yt_dlp.YoutubeDL(video_opts) as ydl:
        for url in URLS:
            try:
                ydl.download([url])
            except:
                continue
    
    with yt_dlp.YoutubeDL(playlist_opts) as ydl:
        for playlist in PLAYLISTS:
            try:
                ydl.download([playlist])
            except:
                continue

if __name__ == "__main__":
    main()