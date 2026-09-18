"""Cross-platform autostart management.

Supports:
- Linux: .desktop file in ~/.config/autostart/
- Windows: .lnk shortcut in Startup folder
- macOS: LaunchAgent plist (pass)
"""

import os
import sys
import platform
from pathlib import Path
from typing import Optional


def get_autostart_path() -> Path:
    """Get the autostart file/directory path for current OS."""
    system = platform.system()

    if system == "Linux":
        return Path.home() / ".config" / "autostart" / "devtime.desktop"

    elif system == "Windows":
        return (
                Path(os.environ["APPDATA"])
                / "Microsoft"
                / "Windows"
                / "Start Menu"
                / "Programs"
                / "Startup"
                / "DevTimeTracker.lnk"
        )

    elif system == "Darwin":
        return Path.home() / "Library" / "LaunchAgents" / "com.devtime.tracker.plist"
    
    else:
        raise OSError(f"Unsupported OS: {system}")

