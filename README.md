# Music Downloader Pro

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-FF0000?style=flat&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)
[![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=flat&logo=spotify&logoColor=white)](https://developer.spotify.com/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat&logo=ffmpeg&logoColor=white)](https://ffmpeg.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/PierrunoYT/music-downloader-pro/commits/master)

A Flask web application that downloads audio from both YouTube videos and Spotify tracks. YouTube content is downloaded in high-quality Opus format using yt-dlp, while Spotify tracks are downloaded in M4A format using spotdl.

## 🎯 Features

- 🎨 Clean, simple web interface
- 🎵 Support for both YouTube videos and Spotify tracks
- 🎧 High-quality audio extraction
  - YouTube: Opus format (251/bestaudio)
  - Spotify: M4A format (320k bitrate)
- 🔒 Secure file downloads
- ✅ Input validation and error handling
- 🚀 Uses official Spotify API and yt-dlp for downloads
- 📁 Unique filename generation with timestamps
- 🔍 Smart URL parsing for both platforms

## 🖼️ Preview

Access the application through your web browser at `http://localhost:8000` after installation.

The application features a simple interface with:
- URL input field for both YouTube and Spotify links
- Clear success/error status messages
- Direct download links for converted files
- Support for both youtu.be and youtube.com URL formats

## 🔧 Prerequisites

- Python 3.7+
- Spotify API credentials (Client ID and Secret)
- FFmpeg (for audio conversion)
- spotdl for Spotify downloads
- yt-dlp for YouTube downloads

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/PierrunoYT/music-downloader-pro.git
cd music-downloader-pro
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Install FFmpeg:
   - Windows: Download from [FFmpeg website](https://ffmpeg.org/download.html) and add to PATH
   - Linux: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`

5. Set up Spotify API:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new application
   - Get your Client ID and Client Secret

6. Configure environment variables:
   Create a `.env` file in the project root with the following:
   ```
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   ```

## 🚀 Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:8000`

3. Choose your source:
   - For YouTube: Paste a YouTube video URL
   - For Spotify: Paste a Spotify track URL

4. Click "Convert" and wait for the process to complete

5. Click the download link to get your converted audio file

## 📺 YouTube Features

- **Video Download**: Convert individual YouTube videos to Opus format
- **Format Selection**: Automatically selects the best audio quality (format 251)
- **URL Support**:
  - Standard youtube.com URLs
  - Short youtu.be URLs
- **Metadata Extraction**:
  - Video title
  - Description
- **Safe File Handling**:
  - Unique filename generation
  - Timestamp-based naming
  - Filename sanitization

## 🎵 Spotify Features

- **Track Download**: Convert individual Spotify tracks to M4A format
- **High Quality**: 320kbps bitrate audio
- **Metadata Preservation**:
  - Track title
  - Artist name
- **Safe File Handling**:
  - Temporary directory usage
  - Automatic cleanup
  - Unique filename generation

## 🔧 Technical Details

- Flask web framework for the backend
- yt-dlp for YouTube video downloading
- spotdl for Spotify track downloading
- Spotipy for Spotify API integration
- FFmpeg for audio processing
- Logging system for debugging
- Error handling and input validation
- Secure file operations
- Clean project structure:
  - `app.py`: Main Flask application
  - `spotify_utils.py`: Spotify-related functionality
  - `youtube_utils.py`: YouTube-related functionality
  - `url_utils.py`: URL parsing and validation
  - `file_utils.py`: File operations and safety

## ⚠️ Error Handling

The application includes error handling for:
- Invalid YouTube/Spotify URLs
- Missing or invalid API credentials
- Download failures
- File system errors
- Network issues
- Invalid input validation

## 🔒 Security Features

- Input validation and sanitization
- Safe file handling with unique filenames
- Secure downloads with proper MIME types
- Environment variable configuration
- Temporary file cleanup
- Sanitized file paths

## 🔍 Troubleshooting

Common issues and solutions:

1. **Spotify API Issues**
   - Verify your Client ID and Secret in `.env`
   - Ensure the Spotify API credentials are valid
   - Check if the track is available in your region

2. **YouTube Download Issues**
   - Ensure you're using a valid video URL
   - Check your internet connection
   - Verify FFmpeg is properly installed

3. **File Download Issues**
   - Ensure the downloads directory exists
   - Check file permissions
   - Verify disk space availability

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 PierrunoYT

## ⚠️ Disclaimer

This tool is for personal use only. Please respect YouTube's and Spotify's terms of service and content creators' rights when using this application.
