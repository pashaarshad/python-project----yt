from flask import Flask, render_template, request, redirect, url_for
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    # Get the YouTube URL from the form
    video_url = request.form['video_url']

    if video_url:
        # Options for downloading
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',  # Save the video using its title
        }

        try:
            # Use yt_dlp to download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            return "Download complete!"
        except Exception as e:
            return f"An error occurred: {e}"

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
