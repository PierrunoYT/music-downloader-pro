import yt_dlp
import logging
import os

logger = logging.getLogger(__name__)

def get_video_info(video_url):
    """Get video or playlist information using yt-dlp."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
            if 'entries' in info:  # It's a playlist
                return {
                    'type': 'playlist',
                    'title': info.get('title', ''),
                    'entries': [
                        {'title': entry.get('title', '')}
                        for entry in info['entries']
                    ]
                }
            else:  # It's a single video
                return {
                    'type': 'video',
                    'title': info.get('title', ''),
                    'description': info.get('description', '')
                }
    except Exception as e:
        raise ValueError(f"Failed to get video info: {str(e)}")

def download_audio(video_url, output_path):
    """Download raw audio using yt-dlp."""
    output_path = os.path.splitext(output_path)[0] + '.webm'
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        raise ValueError(f"Download failed: {str(e)}")
