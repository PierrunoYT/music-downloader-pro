# YouTube to MP3 Downloader

[![yt-dlp](https://img.shields.io/badge/yt--dlp-2024.10.7-red.svg)](https://github.com/yt-dlp/yt-dlp/releases/tag/2024.10.7)

This is a Python script with a web interface that allows you to download the audio from YouTube videos and save them as MP3 files.

## Features

- Download audio from YouTube videos
- Convert audio to MP3 format
- User-friendly web interface
- Command-line interface support
- Progress bar for download status
- Custom output directory selection
- YouTube URL validation
- Responsive design for mobile and desktop

## Requirements

- Python 3.6+
- yt-dlp (version 2024.10.7)
- FFmpeg
- Modern web browser

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Youtube2MP3.git
   cd Youtube2MP3
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have FFmpeg installed on your system. If not, you can download it from [here](https://ffmpeg.org/download.html).

## Usage

### Web Interface

1. Open the `frontend/index.html` file in your web browser
2. Enter the YouTube URL in the input field
3. Click the "Download" button
4. The MP3 file will be downloaded to your specified directory

### Command Line Interface

Run the script using Python:

```
python youtube_to_mp3.py
```

1. When prompted, enter the URL of the YouTube video you want to download.
2. Enter the output directory where you want to save the MP3 file (press Enter to use the current directory).
3. The script will download the audio, display the progress, and save it as an MP3 file in the specified directory.

## Updating yt-dlp

To update yt-dlp to the latest version, run:

```
pip install --upgrade yt-dlp
```

Then update the version in the `requirements.txt` file:

```
yt-dlp==<new_version>
```

## Development

### Setting up the development environment

1. Fork the repository on GitHub.
2. Clone your forked repository locally.
3. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the development dependencies:
   ```
   pip install -r requirements.txt
   ```

### Project Structure

```
Youtube2MP3/
├── frontend/               # Web interface files
│   ├── index.html         # Main HTML file
│   ├── styles.css         # CSS styles
│   └── script.js          # Frontend JavaScript
├── youtube_to_mp3.py      # Main Python script
├── requirements.txt       # Python dependencies
└── tests/                # Test files
```

### Running tests

To run the tests, execute:

```
python -m unittest discover tests
```

### Making changes

1. Create a new branch for your feature or bug fix.
2. Make your changes and commit them with a clear commit message.
3. Push your changes to your fork on GitHub.
4. Create a pull request to the main repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is for personal use only. Please respect copyright laws and YouTube's terms of service.
