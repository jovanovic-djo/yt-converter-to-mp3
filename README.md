# Youtube to mp3 Converter

A simple Python script to batch convert YouTube videos to MP3 format.

## Features

- Batch processing of individual YouTube videos
- Full playlist download and conversion
- Automatic directory creation
- Clean and minimal codebase

## Requirements

- Python 3.6
- yt-dlp

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/youtube-to-mp3-converter.git
cd youtube-to-mp3-converter
```

2. Install Python dependencies:
```bash
pip install yt-dlp
```

## Usage

1. Create and edit `data.py` and add your YouTube URLs and/or playlists:
```python
# Individual videos
youtube_urls = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",

]

# Entire playlists
youtube_playlists = [
    "https://www.youtube.com/playlist?",

]
```

2. Run the converter:
```bash
python main.py
```


## Disclaimer

This tool is for educational purposes only. Users are responsible for ensuring they comply with YouTube's Terms of Service and applicable copyright laws when downloading content.
