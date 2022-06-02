from __future__ import unicode_literals
import youtube_dl


# Retrieve the mp4 file
def get_vidfile():
    download_options = {}
    yt_vid_url = input("Enter the URL of the YouTube video you want to download.\n").strip()
    with youtube_dl.YoutubeDL(download_options) as ydl:
        ydl.download([yt_vid_url])

get_vidfile()