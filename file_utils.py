import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def generate_unique_filename(original_filename, extension):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base = os.path.splitext(original_filename)[0]
    return f"{base}_{timestamp}{extension}"

def ensure_downloads_dir(base_dir):
    """Ensure downloads directory exists and return its path."""
    downloads_dir = os.path.join(base_dir, 'downloads')
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
        logger.info(f"Created downloads directory at: {downloads_dir}")
    return downloads_dir

def sanitize_filename(title):
    """Create a safe filename from a title."""
    return "".join([c for c in title if c.isalnum() or c in (' ', '-', '_', '.')]).rstrip()
