from flask import Flask, request, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def download():
    video_url = request.form['video_url']
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    audio_file = stream.download()
    return render_template('index.html', audio_file=audio_file)

if __name__ == '__main__':
    app.run(debug=True)
