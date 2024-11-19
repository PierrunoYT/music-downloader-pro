# Music Downloader Pro

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://developers.google.com/youtube/v3)
[![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=flat&logo=spotify&logoColor=white)](https://developer.spotify.com/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat&logo=ffmpeg&logoColor=white)](https://ffmpeg.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/PierrunoYT/music-downloader-pro/commits/master)

A powerful Flask web application that converts both YouTube videos and Spotify tracks to MP3 format. Utilizing YouTube Data API, yt-dlp, and Spotify API for high-quality audio extraction.

## 🎯 Features

- 🎨 Clean, modern user interface
- 🎵 Support for both YouTube videos and Spotify tracks
- 🎧 High-quality audio extraction
- 🔄 Real-time conversion progress updates
- 🔒 Secure file downloads
- ✅ Input validation and error handling
- 🚀 Uses official YouTube Data API and Spotify API
- 📁 Unique filename generation with timestamps
- 📺 YouTube playlist support
- 🎶 Spotify playlist support
- 🏷️ Automatic metadata tagging

## 🖼️ Preview

Access the application through your web browser at `http://localhost:5000` after installation.

The application features a clean, intuitive interface with:
- Simple URL input field for both YouTube and Spotify links
- Real-time progress tracking with visual feedback
- Clear download status indicators
- Responsive design that works on both desktop and mobile
- Dark/light mode support
- Easy-to-use playlist handling interface

## 🔧 Prerequisites

- Python 3.7+
- YouTube Data API key
- Spotify API credentials (Client ID and Secret)
- FFmpeg (for audio conversion)

## 📦 Installation

1. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

2. Clone the repository:
```bash
git clone https://github.com/PierrunoYT/music-downloader-pro.git
cd music-downloader-pro
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Install FFmpeg:
   - Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add to PATH
   - Linux: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`

5. Set up YouTube Data API:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the YouTube Data API v3
   - Create credentials (API key)
   - Set up API restrictions and quotas

6. Set up Spotify API:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new application
   - Get your Client ID and Client Secret
   - Add `http://localhost:5000/callback` to your Redirect URIs

7. Configure environment variables:
   Create a `.env` file in the project root with the following:
   ```
   YOUTUBE_API_KEY=your_youtube_api_key
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   ```

## 🚀 Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Choose your source:
   - For YouTube: Paste a YouTube URL (video or playlist)
   - For Spotify: Paste a Spotify track or playlist URL

4. Click "Convert" and wait for the process to complete

5. Download your converted MP3 file(s)

## 📺 YouTube Features

- **Video Download**: Convert individual YouTube videos to MP3
- **Playlist Support**: Download entire YouTube playlists
- **Quality Options**: Choose between different audio quality settings
  - High Quality (256kbps)
  - Standard Quality (128kbps)
  - Custom Quality Settings
- **Format Selection**: Automatically selects the best audio format
- **Metadata Extraction**:
  - Video title as track name
  - Channel name as artist
  - Upload date
  - Description
  - Thumbnails
- **Advanced Features**:
  - Timestamp support for partial downloads
  - Automatic chapter detection
  - Custom filename templates
  - Batch processing for playlists
  - Progress tracking for long videos
  - Resume interrupted downloads

## 🎵 Spotify Features

- **Track Download**: Convert individual Spotify tracks to MP3
- **Playlist Support**: Download entire Spotify playlists
- **Metadata Preservation**: Maintains artist, album, and track information
- **Album Artwork**: Automatically embeds album covers
- **Smart Search**: Finds the best matching audio source for Spotify tracks
- **Batch Processing**: Efficiently handles multiple tracks from playlists
- **Advanced Features**:
  - Album support
  - Artist discography download
  - Playlist folder organization
  - Custom metadata templates
  - Regional availability check

## 🔧 Technical Details

- Flask web framework for the backend
- YouTube Data API v3 for video information
- yt-dlp for YouTube video downloading
- Spotify Web API for track and playlist information
- spotdl for Spotify track downloading
- FFmpeg for audio extraction and conversion
- Bootstrap 5 for responsive design
- Font Awesome for icons
- Real-time progress updates using WebSocket
- Efficient caching system
- Rate limiting implementation
- Queue management for batch processing

## ⚠️ Error Handling

The application includes comprehensive error handling for:
- Invalid YouTube/Spotify URLs
- Private or unavailable videos/tracks
- API quota exceeded
- Invalid API credentials
- Network issues
- File system errors
- Spotify authentication issues
- Geoblocked content
- Rate limiting
- Corrupted downloads
- Insufficient disk space

## 🔒 Security Features

- Input validation and sanitization
- Safe file handling with unique filenames
- Secure downloads
- Environment variable configuration
- No temporary file exposure
- Secure Spotify OAuth implementation
- Rate limiting
- Request validation
- XSS protection
- CSRF protection

## 🔍 Troubleshooting

Common issues and solutions:

1. **FFmpeg not found**
   - Ensure FFmpeg is properly installed and added to your system's PATH
   - Try running `ffmpeg -version` in your terminal to verify the installation
   - Check FFmpeg codecs support

2. **YouTube API Issues**
   - Verify your API key is correctly set in the `.env` file
   - Check if you've enabled the YouTube Data API v3
   - Monitor your API quota usage
   - Ensure proper API restrictions are set
   - Check for regional restrictions

3. **Spotify Authentication Issues**
   - Verify your Spotify Client ID and Secret
   - Check if the redirect URI is properly configured
   - Ensure your Spotify application is properly set up
   - Verify token refresh mechanism

4. **Download Issues**
   - Check your internet connection
   - Verify the content is available in your region
   - Ensure you have sufficient disk space
   - Check if the content is age-restricted
   - Verify file permissions
   - Check for rate limiting

## 👥 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 PierrunoYT

## ⚠️ Disclaimer

This tool is for personal use only. Please respect YouTube's and Spotify's terms of service and content creators' rights when using this application.
