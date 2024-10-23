import os
import re
import yt_dlp

def is_valid_youtube_url(url):
    """
    Check if the provided URL is a valid YouTube URL.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    return re.match(youtube_regex, url) is not None

def download_progress_hook(d):
    """
    Callback function to display download progress.

    Args:
        d (dict): Dictionary containing download information.
    """
    if d['status'] == 'downloading':
        percent = d['_percent_str']
        speed = d['_speed_str']
        eta = d['_eta_str']
        print(f'\rDownloading... {percent} (Speed: {speed}, ETA: {eta})', end='', flush=True)
    elif d['status'] == 'finished':
        print('\nDownload finished. Converting...')

def download_youtube_audio(url, output_path=None, format='mp3'):
    """
    Download audio from a YouTube video and save it as an audio file.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str): The directory to save the downloaded audio. Defaults to 'downloads' folder.
        format (str): The output audio format ('mp3' or 'wav'). Defaults to 'mp3'.

    Returns:
        None
    """
    if not is_valid_youtube_url(url):
        print("Error: Invalid YouTube URL")
        return

    if format not in ['mp3', 'wav']:
        print("Error: Unsupported format. Use 'mp3' or 'wav'")
        return

    # Use downloads folder as default if no path specified
    if output_path is None or not output_path.strip():
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': '192' if format == 'mp3' else None,
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'progress_hooks': [download_progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nDownload and conversion to {format.upper()} completed successfully!")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

def main():
    """
    Main function to run the YouTube audio downloader.
    """
    url = input("Enter the YouTube URL you want to download: ")
    output_path = input("Enter the output directory (press Enter for downloads folder): ").strip()
    format_choice = input("Enter the output format (mp3/wav, default: mp3): ").strip().lower()
    
    if not format_choice:
        format_choice = 'mp3'
    
    download_youtube_audio(url, output_path, format_choice)

if __name__ == "__main__":
    main()
