# YouTube to MP3 Downloader

This is a simple Python command-line tool to download YouTube videos and convert them to MP3 format.

## Prerequisites

- Python 3.6 or higher
- ffmpeg (must be installed and available in your system PATH)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/youtube-to-mp3.git
   cd youtube-to-mp3
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To download a YouTube video and convert it to MP3, run:

```
python youtube_to_mp3.py
```

You will be prompted to enter the YouTube URL of the video you want to download.

The MP3 file will be saved in the current directory with the video's title as the filename.

## Example

When you run the script, you'll see:

```
Enter the YouTube URL you want to download: 
```

Then, you can paste or type the URL, for example:
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

This will download the audio from the video and save it as an MP3 file in the current directory.

## Note

Please ensure you have the right to download and convert the YouTube content. Respect copyright laws and YouTube's terms of service.

## Deactivating the Virtual Environment

When you're done using the tool, you can deactivate the virtual environment by running:

```
deactivate
```

This will return you to your global Python environment.
