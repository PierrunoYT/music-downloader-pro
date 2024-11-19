import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import logging
import os
import subprocess
import shutil

logger = logging.getLogger(__name__)

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.spotify = None
        
        if client_id and client_secret:
            try:
                self.spotify = spotipy.Spotify(
                    client_credentials_manager=SpotifyClientCredentials(
                        client_id=client_id,
                        client_secret=client_secret
                    )
                )
                logger.info("Successfully initialized Spotify client")
            except Exception as e:
                logger.error(f"Failed to initialize Spotify client: {str(e)}")

    def get_track_info(self, track_id):
        """Get track information using Spotify API."""
        if not self.spotify:
            raise ValueError("Spotify API credentials not configured")
        
        try:
            track = self.spotify.track(track_id)
            return {
                'title': track['name'],
                'artist': track['artists'][0]['name']
            }
        except Exception as e:
            logger.error(f"Failed to get track info: {str(e)}")
            raise ValueError(f"Spotify API error: {str(e)}")
            
    def search_track(self, query):
        """Search for a track using Spotify API."""
        if not self.spotify:
            raise ValueError("Spotify API credentials not configured")
            
        try:
            results = self.spotify.search(q=query, type='track', limit=5)
            tracks = []
            
            for track in results['tracks']['items']:
                tracks.append({
                    'id': track['id'],
                    'title': track['name'],
                    'artist': track['artists'][0]['name'],
                    'url': track['external_urls']['spotify']
                })
            
            return tracks
        except Exception as e:
            logger.error(f"Failed to search tracks: {str(e)}")
            raise ValueError(f"Spotify API error: {str(e)}")
            
    def get_playlist_info(self, playlist_id):
        """Get playlist information using Spotify API."""
        if not self.spotify:
            raise ValueError("Spotify API credentials not configured")
        
        try:
            playlist = self.spotify.playlist(playlist_id)
            tracks = []
            
            # Get all tracks from playlist
            results = playlist['tracks']
            while results:
                for item in results['items']:
                    if item['track']:
                        tracks.append({
                            'title': item['track']['name'],
                            'artist': item['track']['artists'][0]['name']
                        })
                results = self.spotify.next(results) if results['next'] else None
            
            return {
                'type': 'playlist',
                'title': playlist['name'],
                'tracks': tracks
            }
        except Exception as e:
            logger.error(f"Failed to get playlist info: {str(e)}")
            raise ValueError(f"Spotify API error: {str(e)}")

def download_spotify_track(track_url, output_path, client_id, client_secret):
    """Download Spotify track using spotdl CLI with high quality M4A."""
    if not client_id or not client_secret:
        raise ValueError("Spotify API credentials not configured")
    
    try:
        temp_dir = os.path.join(os.path.dirname(output_path), 'temp')
        os.makedirs(temp_dir, exist_ok=True)
        
        try:
            command = [
                'spotdl',
                '--client-id', client_id,
                '--client-secret', client_secret,
                '--output', temp_dir,
                '--format', 'ogg',  # Original Spotify format
                '--bitrate', '320k',  # Set highest quality bitrate
                track_url
            ]
            
            result = subprocess.run(command, capture_output=True, text=True)
            
            if result.returncode != 0:
                logger.error(f"spotdl command failed: {result.stderr}")
                raise ValueError("Failed to download track")
            
            downloaded_files = os.listdir(temp_dir)
            if not downloaded_files:
                raise ValueError("No file was downloaded")
            
            downloaded_file = os.path.join(temp_dir, downloaded_files[0])
            shutil.move(downloaded_file, output_path)
            
            logger.info(f"Successfully downloaded track to {output_path}")
            
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
            
    except Exception as e:
        logger.error(f"Download failed with error: {str(e)}")
        raise ValueError(f"Download failed: {str(e)}")
