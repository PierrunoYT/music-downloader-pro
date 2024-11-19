from flask import Flask, request, render_template, send_file
import os
from dotenv import load_dotenv
import logging
from url_utils import extract_video_id, is_spotify_url, extract_spotify_track_id
from file_utils import generate_unique_filename, ensure_downloads_dir, sanitize_filename
from youtube_utils import download_audio, get_video_info
from spotify_utils import SpotifyAPI, download_spotify_track

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_url_path='/static')

# Get the absolute path of the current directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DOWNLOADS_DIR = ensure_downloads_dir(BASE_DIR)

# API configurations
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID', '')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET', '')

# Initialize Spotify API
spotify_api = SpotifyAPI(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert():
    try:
        url = request.form.get('url')
        if not url:
            raise ValueError("Please provide a valid URL")
        
        # Check if it's a Spotify URL
        if is_spotify_url(url):
            if not spotify_api.spotify:
                raise ValueError("Spotify downloads are not configured")
            
            # Extract track ID and validate
            track_id = extract_spotify_track_id(url)
            if not track_id:
                raise ValueError("Invalid Spotify track URL")
            
            # Get track information
            track_info = spotify_api.get_track_info(track_id)
            
            # Generate safe filename
            title = f"{track_info['artist']} - {track_info['title']}"
            safe_title = sanitize_filename(title)
            unique_filename = generate_unique_filename(safe_title, '.m4a')
            output_path = os.path.join(DOWNLOADS_DIR, unique_filename)
            
            # Download track
            download_spotify_track(url, output_path, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
            
        else:
            # Handle as YouTube URL
            video_id = extract_video_id(url)
            if not video_id:
                raise ValueError("Invalid YouTube URL")
            
            # Get video information
            video_info = get_video_info(url)
            
            # Generate safe filename
            title = video_info['title']
            safe_title = sanitize_filename(title)
            unique_filename = generate_unique_filename(safe_title, '.mp3')
            output_path = os.path.join(DOWNLOADS_DIR, unique_filename)
            
            # Download audio
            download_audio(url, output_path)
        
        return render_template(
            'index.html',
            success=True,
            filename=unique_filename,
            video_title=title
        )
        
    except ValueError as e:
        logger.error(f"Error processing request: {str(e)}")
        return render_template('index.html', error=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        error_message = "An unexpected error occurred. Please try again later."
        if app.debug:
            error_message = str(e)
        return render_template('index.html', error=error_message)

@app.route('/download/<filename>')
def download(filename):
    try:
        file_path = os.path.join(DOWNLOADS_DIR, filename)
        
        if not os.path.exists(file_path):
            logger.error(f"File not found at path: {file_path}")
            return "File not found", 404
        
        # Set correct MIME type based on file extension
        mime_type = 'audio/mpeg' if filename.endswith('.mp3') else 'audio/mp4'
            
        return send_file(
            file_path,
            mimetype=mime_type,
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        logger.error(f"Error during file download: {str(e)}")
        return str(e), 404

if __name__ == "__main__":
    if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
        logger.warning("Spotify API credentials not set")
    app.run(host="0.0.0.0", port=8000, debug=True)
