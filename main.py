import os
import shutil
import sys
import yt_dlp

try:
    from data import URLS, PLAYLISTS
except ImportError:
    URLS = [
        # "https://www.youtube.com/watch?v=xxxxxxxxxxx",
    ]
    PLAYLISTS = [

    ]


def find_ffmpeg():
    if shutil.which("ffmpeg") and shutil.which("ffprobe"):
        return None

    try:
        import ffmpeg_downloader as ffdl
        if os.path.isfile(ffdl.ffmpeg_path) and os.path.isfile(ffdl.ffprobe_path):
            return os.path.dirname(ffdl.ffmpeg_path)
    except ImportError:
        pass

    return False


def build_opts(is_playlist: bool, ffmpeg_loc=None) -> dict:
    opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'converted/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': not is_playlist,
        'ignoreerrors': True, 
        'restrictfilenames': True,   
        'download_archive': 'converted/.archive.txt',

        'quiet': False,
    }
    if ffmpeg_loc:
        opts['ffmpeg_location'] = ffmpeg_loc
    return opts


def download_all(urls, opts, label):
    if not urls:
        return
    with yt_dlp.YoutubeDL(opts) as ydl:
        for url in urls:
            print(f"\n--- {label}: {url} ---")
            try:
                ydl.download([url])
            except Exception as e:
                print(f"  Skipped ({e})")


def main():
    ffmpeg_loc = find_ffmpeg()
    if ffmpeg_loc is False:
        print(
            "ffmpeg/ffprobe not found -- files would download but stay as "
            ".webm/.m4a instead of converting to .mp3.\n"
            "Install it in this venv with:\n"
            "  pip install ffmpeg-downloader\n"
            "  ffdl install --add-path\n"
            "(then reopen your terminal / reactivate the venv)."
        )
        sys.exit(1)

    os.makedirs("converted", exist_ok=True)

    if not URLS and not PLAYLISTS:
        print("Nothing to download. Add links to data.py (or directly in main.py).")
        return

    download_all(URLS, build_opts(is_playlist=False, ffmpeg_loc=ffmpeg_loc), "video")
    download_all(PLAYLISTS, build_opts(is_playlist=True, ffmpeg_loc=ffmpeg_loc), "playlist")

    print("\nDone.")


if __name__ == "__main__":
    main()