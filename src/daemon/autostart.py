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


def is_enabled() -> bool:
    """Check if autostart is enabled."""
    return get_autostart_path().exists()


def enable() -> bool:
    """Enable autostart."""
    system = platform.system()

    if system == "Linux":
        return _enable_linux()

    elif system == "Windows":
        return _enable_windows()

    elif system == "Darwin":
        return _enable_macos()

    return False


def disable() -> bool:
    """Disable autostart."""
    path = get_autostart_path()

    if path.exists():
        path.unlink()
        return True

    return False


def _enable_linux() -> bool:
    """Enable autostart on Linux using .desktop file."""
    pass


def _enable_windows() -> bool:
    """Enable autostart on Windows using Startup folder."""
    pass


def _enable_macos() -> bool:
    """Enable autostart on macOS using LaunchAgent."""
    pass

