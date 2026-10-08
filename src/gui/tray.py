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

    def _start_tracker(self, icon, item):
        """Start the tracker in a separate thread."""
        if self.tracker_thread and self.tracker_thread.is_alive():
            print("⚠️ Tracker is already running")
            return

        self.tracker_thread = threading.Thread(
            target=self.tracker.start,
            daemon=True
        )
        self.tracker_thread.start()
        print("▶️ Tracker started")

        if self.icon:
            self.icon.icon = create_icon('green')

    def _stop_tracker(self, icon, item):
        """Stop the tracker."""
        self.tracker.stop()
        print("⏹️ Tracker stopped")

        if self.icon:
            self.icon.icon = create_icon('red')

    def _show_stats(self, icon, item):
        """Show statistics window."""
        from src.gui.window import
        show_stats_window(self.tracker.storage)

    def _quit(self, icon, item):
        """Quit the aplication."""
        if self.tracker.is_running:
            self.tracker.stop()
        icon.stop()

    def run(self):
        """Run the tray icon."""
        menu = pystray.Menu(
            item('▶️ Start Tracking', self._start_tracker),
            item('⏹️ Stop Tracking', self._stop_tracker),
            pystray.Menu.SEPARATOR,
            item('📊 Show Statistics', self._show_stats),
            pystray.Menu.SEPARATOR,
            item('❌ Quit', self._quit),
        )

        self.icon = pystray.Icon(
            "DevTimeTracker",
            create_icon('red'),
            "DevTimeTracker",
            menu
        )

        print("🚀 Tray icon started")
        self.icon.run()


        )