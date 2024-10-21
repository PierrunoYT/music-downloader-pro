import os
import sys
import youtube_dl

def download_youtube_audio(url, output_path='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    if len(sys.argv) < 2:
        print("Usage: python youtube_to_mp3.py <YouTube URL>")
        sys.exit(1)

    url = sys.argv[1]
    download_youtube_audio(url)

if __name__ == "__main__":
    main()
