import unittest
import os
from youtube_to_mp3 import is_valid_youtube_url, download_youtube_audio

class TestYoutubeToMP3(unittest.TestCase):
    def test_is_valid_youtube_url(self):
        valid_urls = [
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'https://youtu.be/dQw4w9WgXcQ',
            'https://www.youtube.com/embed/dQw4w9WgXcQ'
        ]
        invalid_urls = [
            'https://www.example.com',
            'https://www.youtube.com',
            'https://www.youtube.com/watch?v=invalid'
        ]
        
        for url in valid_urls:
            self.assertTrue(is_valid_youtube_url(url))
        
        for url in invalid_urls:
            self.assertFalse(is_valid_youtube_url(url))

    def test_download_youtube_audio(self):
        # Use a short, public domain video for testing
        test_url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
        test_output_path = 'test_output'
        
        if not os.path.exists(test_output_path):
            os.makedirs(test_output_path)
        
        download_youtube_audio(test_url, test_output_path)
        
        # Check if any .mp3 file was created in the output directory
        mp3_files = [f for f in os.listdir(test_output_path) if f.endswith('.mp3')]
        self.assertTrue(len(mp3_files) > 0)
        
        # Clean up
        for file in mp3_files:
            os.remove(os.path.join(test_output_path, file))
        os.rmdir(test_output_path)

if __name__ == '__main__':
    unittest.main()
