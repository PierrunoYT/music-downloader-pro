from urllib.parse import urlparse, parse_qs
import re
import logging

logger = logging.getLogger(__name__)

def extract_video_id(url):
    """Extract the video ID or playlist ID from a YouTube URL."""
    if not url:
        return None
        
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    # Handle playlist URLs
    if 'list' in query_params:
        return {'type': 'playlist', 'id': query_params['list'][0]}
        
    # Handle youtu.be URLs
    if 'youtu.be' in parsed_url.netloc:
        return {'type': 'video', 'id': url.split('/')[-1]}
        
    # Handle youtube.com URLs
    if 'youtube.com' in parsed_url.netloc:
        video_id = query_params.get('v', [None])[0]
        if video_id:
            return {'type': 'video', 'id': video_id}
        
    return None

def is_spotify_url(url):
    """Check if the URL is a Spotify track or playlist URL."""
    parsed_url = urlparse(url)
    return 'spotify.com' in parsed_url.netloc and ('/track/' in parsed_url.path or '/playlist/' in parsed_url.path)

def extract_spotify_id(url):
    """Extract track or playlist ID from Spotify URL."""
    if not url:
        return None
    
    # Check for playlist
    playlist_match = re.search(r'/playlist/([a-zA-Z0-9]+)(?:\?|/|$)', url)
    if playlist_match:
        playlist_id = playlist_match.group(1)
        if '?' in playlist_id:
            playlist_id = playlist_id.split('?')[0]
        return {'type': 'playlist', 'id': playlist_id}
    
    # Check for track
    track_match = re.search(r'/track/([a-zA-Z0-9]+)(?:\?|/|$)', url)
    if track_match:
        track_id = track_match.group(1)
        if '?' in track_id:
            track_id = track_id.split('?')[0]
        return {'type': 'track', 'id': track_id}
    
    return None
