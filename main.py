import os
import yt_dlp
from data import URLS


"""
        # You can add your songs/content to this playlist.
URLS = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
]
"""

def main():
    os.makedirs("converted", exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'converted/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in URLS:
            try:
                ydl.download([url])
            except:
                continue

if __name__ == "__main__":
    main()