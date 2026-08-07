"""
Cross-platform window management module.

This module provides a unified interface for window detection across
different operating system. It automatically selects the appropriate
backed based on the current platform.

Supported platforms:
- Linux: Uses xdotool (requires installation)
- Windows: Uses pygetwindow library
- macOS: Uses appleScript( native)

Example:
    >>> from src.core.window_manager import get_all_windows, Window
    >>> windows = get_all_windows()
    >>> for win in windows:
    ...     print(f"{win.title} (active: {win.isActive})")
"""

import sys
import subprocess
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class Window:
    """
    Represents a system windows.

    Attributes:
        window_id: Unique identifier for the window.
        title: Window title text/
        isActive: Whether the window is currently in focus.
    """
    window_id: str
    title: str
    isActive: bool = False


def _get_windows_linux() -> List[Window]:
    """
    Get all windows on Linux using xdotool.

    This function uses the xdotool command-line tool to query window
    information. It returns a list of all visible windows.

    Returns:
        List of Window objects for all windows found.

    Note:
        Requires xdotool to be installed:
        sudo apt-get install xdotool
    """
    try:
        # Verify xdotool is installed
        subprocess.run(['xdotool', '--version'], capture_output=True, check=True)

        # Get all window IDs
        result = subprocess.run(
            ['xdotool', 'search', '--name', '.*'],
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode != 0 or not result.stdout:
            return []

        window_ids = result.stdout.strip().split('\n')
        windows = []

        # Get the active window ID
        active_result = subprocess.run(
            ['xdotool', 'getactivewindow'],
            capture_output=True,
            text=True,
            check=False
        )
        active_window_id = active_result.stdout.strip() if active_result.returncode == 0 else None

        for window_id in window_ids:
            if not window_id:
                continue

            # Get the window title
            title_result = subprocess.run(
                ['xdotool', 'getwindowname', window_id],
                capture_output=True,
                text=True,
                check=False
            )

            if title_result.returncode == 0 and title_result.stdout:
                title = title_result.stdout.strip()
                is_active = (window_id == active_window_id)

                windows.append(Window(
                    window_id=window_id,
                    title=title,
                    isActive=is_active
                ))

        return windows

    except (subprocess.CalledProcessError, FileNotFoundError):
        # xdotool not installed or failed
        return []


def _get_windows_windows():
    try:
        import pygetwindow as gw

        windows = []
        for w in gw.getAllWindows():
            if w.title:
                windows.append(Window(
                    window_id=str(w._hWnd),
                    title=w.title,
                    isActive=w.isActive
                ))
        return windows

    except ImportError:
        return []


def _get_windows_macos():
    try:
        script = '''
        tell application "System Events"
            get name of every window of every process
        and tell
        
        '''
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode != 0 or not result.stdout:
            return []

        return []

    except (subprocess.CalledProcessError, FileNotFoundError):
        return []


def get_all_windows():
    system = sys.platform

    if system == 'linux':
        return _get_windows_linux()
    elif system == 'win32':
        return _get_windows_windows()
    elif system == 'darwin':
        return _get_windows_macos()
    else:
        return []


def get_active_windows():
    windows = get_all_windows()
    for window in windows:
        if window.isActive:
            return window
    return None