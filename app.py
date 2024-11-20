from flask import Flask, request, render_template, send_file
import os
from dotenv import load_dotenv
import logging
from url_utils import extract_video_id, is_spotify_url, extract_spotify_id
from file_utils import ensure_downloads_dir, sanitize_filename
from youtube_utils import download_audio, get_video_info
from spotify_utils import SpotifyAPI, download_spotify_track

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_url_path='', static_folder='static')

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

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return []
        
    try:
        tracks = spotify_api.search_track(query)
        return tracks
    except Exception as e:
        logger.error(f"Search error: {str(e)}")
        return [], 500

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
            
            # Extract ID and validate
            spotify_info = extract_spotify_id(url)
            if not spotify_info:
                raise ValueError("Invalid Spotify URL")
            
            if spotify_info['type'] == 'playlist':
                # Get playlist information
                playlist_info = spotify_api.get_playlist_info(spotify_info['id'])
                
                # Create playlist directory
                playlist_dir = os.path.join(DOWNLOADS_DIR, sanitize_filename(playlist_info['title']))
                os.makedirs(playlist_dir, exist_ok=True)
                
                # Download each track in playlist
                for track in playlist_info['tracks']:
                    safe_title = sanitize_filename(f"{track['artist']} - {track['title']}")
                    output_path = os.path.join(playlist_dir, f"{safe_title}.ogg")
                    
                    # Construct track URL
                    track_url = f"spotify:track:{track['id']}"
                    download_spotify_track(track_url, output_path, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
                
                # Create zip file of playlist
                zip_filename = f"{sanitize_filename(playlist_info['title'])}.zip"
                zip_path = os.path.join(DOWNLOADS_DIR, zip_filename)
                
                import shutil
                shutil.make_archive(os.path.splitext(zip_path)[0], 'zip', playlist_dir)
                
                # Clean up playlist directory
                shutil.rmtree(playlist_dir)
                
                unique_filename = zip_filename
                title = playlist_info['title']
                
            else:  # Single track
                # Get track information
                track_info = spotify_api.get_track_info(spotify_info['id'])
                
                # Generate filename from title
                title = f"{track_info['artist']} - {track_info['title']}"
                safe_title = sanitize_filename(title)
                unique_filename = f"{safe_title}.ogg"
                output_path = os.path.join(DOWNLOADS_DIR, unique_filename)
                
                # Download track
                download_spotify_track(url, output_path, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
            
        else:
            # Handle as YouTube URL
            url_info = extract_video_id(url)
            if not url_info:
                raise ValueError("Invalid YouTube URL")
            
            # Get video/playlist information
            info = get_video_info(url)
            
            if info['type'] == 'playlist':
                # Create playlist directory
                playlist_dir = os.path.join(DOWNLOADS_DIR, sanitize_filename(info['title']))
                os.makedirs(playlist_dir, exist_ok=True)
                
                # Download each video in playlist
                for entry in info['entries']:
                    safe_title = sanitize_filename(entry['title'])
                    output_path = os.path.join(playlist_dir, f"{safe_title}.webm")
                    download_audio(url, output_path)
                
                # Create zip file of playlist
                zip_filename = f"{sanitize_filename(info['title'])}.zip"
                zip_path = os.path.join(DOWNLOADS_DIR, zip_filename)
                
                import shutil
                shutil.make_archive(os.path.splitext(zip_path)[0], 'zip', playlist_dir)
                
                # Clean up playlist directory
                shutil.rmtree(playlist_dir)
                
                unique_filename = zip_filename
                title = info['title']
                
            else:
                # Single video download
                title = info['title']
                safe_title = sanitize_filename(title)
                unique_filename = f"{safe_title}.webm"
                output_path = os.path.join(DOWNLOADS_DIR, unique_filename)
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
        mime_types = {
            '.webm': 'audio/webm',
            '.ogg': 'audio/ogg',
            '.ico': 'image/x-icon',
            '.png': 'image/png',
            '.svg': 'image/svg+xml',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif'
        }
        
        file_ext = os.path.splitext(filename)[1].lower()
        mime_type = mime_types.get(file_ext, 'application/octet-stream')
            
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
