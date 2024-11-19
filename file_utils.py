import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


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
