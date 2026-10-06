"""
System tray icon for DevTimeTracker.

Provides a system tray icon with menu for controlling the tracker.
"""

import threading
from typing import Optional

from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item

from src.core.tracker import TimeTracker


def create_icon(color: str = 'green') -> Image.Image:
    """
    Create a simple icon programmatically.

    Args:
        color: Icon color ('green' for running, 'red' for stopped).

    Returns:
        PIL Image object.
    """
    # Create Image 64x64
    image = Image.new('RGB', (64, 64), 'white')
    draw = ImageDraw.Draw(image)

    # Paint a circle
    draw.ellipse([8, 8, 56, 56], fill=color, outline='black', width=2)

    # Paint a clock
    draw.line([32, 32, 32, 16], fill='white', width=3)
    draw.line([32, 32, 44, 32], fill='white', width=3)

    return image


class TrayIcon:
    """
    System tray icon for DevTimeTracker.

    Shows an icon in the system tray with a menu for controlling
    the tracker and viewing statistics.
    """

    def __init__(self, tracker: TimeTracker):
        """
        Initialize tray icon.

        Args:
            tracker: TimeTracker instance.
        """
        self.tracker = tracker
        self.icon: Optional[pystray.Icon] = None
        self.tracker_thread: Optional[threading.Thread] = None