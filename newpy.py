import yt_dlp

url = input('Enter the link')

# Options for downloading
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',  # This will save the video using its title
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download complete!")
except Exception as e:
    print(f"An error occurred: {e}")
