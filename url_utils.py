from urllib.parse import urlparse, parse_qs
import re
import logging

logger = logging.getLogger(__name__)

def extract_video_id(url):
    """Extract the video ID from a YouTube URL."""
    if not url:
        return None
        
    # Handle youtu.be URLs
    if 'youtu.be' in url:
        return url.split('/')[-1]
        
    # Handle youtube.com URLs
    parsed_url = urlparse(url)
    if 'youtube.com' in parsed_url.netloc:
        return parse_qs(parsed_url.query).get('v', [None])[0]
        
    return None

def is_spotify_url(url):
    """Check if the URL is a Spotify track URL."""
    parsed_url = urlparse(url)
    return 'spotify.com' in parsed_url.netloc and '/track/' in parsed_url.path

def extract_spotify_track_id(url):
    """Extract track ID from Spotify URL."""
    if not url:
        return None
    
    match = re.search(r'/track/([a-zA-Z0-9]+)(?:\?|/|$)', url)
    if not match:
        return None

    track_id = match.group(1)
    if '?' in track_id:
        track_id = track_id.split('?')[0]
    
    logger.debug(f"Extracted track ID: {track_id} from URL: {url}")
    return track_id
