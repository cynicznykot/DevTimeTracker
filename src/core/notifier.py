"""Cross-platform notification system.

This module provides a unified interface for sending system notifications
across different operating systems.

Supported platforms:
- Linux: Uses notify-send
- Windows: Uses win10toast
- macOS: Uses osascript
"""

import platform
import subprocess


def send_notification(title: str, message: str) -> bool:
    """
    Send a system notification.

    Args:
        title: Notification title.
        message: Notification body.

    Returns:
        True if sent successfully, False otherwise.

    Examples:
        >>> send_notification("DevTimeTracker", "Session started")
        True
    """
    system = platform.system()

    if system == 'Linux':
        return _notify_linux(title, message)
    elif system == 'Windows':
        return _notify_windows(title, message)
    elif system == 'Darwin':
        return _notify_macos(title, message)
    return False


def _notify_linux(title: str, message: str) -> bool:
    """
    Send notification on Linux using notify-send.

    Args:
        title: Notification title.
        message: Notification body.

    Returns:
        True if successful, False otherwise.
    """
    try:
        subprocess.run(
            ['notify-send', title, message],
            check=True,
            capture_output=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def _notify_windows(title: str, message: str) -> bool:
    """
    Send notification on Windows using win10toast.

    Args:
        title: Notification title.
        message: Notification body.

    Returns:
        True if successful, False otherwise.

    Note:
        Requires win10toast: pip install win10toast
    """
    try:
        from win10toast import ToastNotifier
    except ImportError:
        return False

    try:
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=5, threading=True)
        return True
    except Exception:
        return False


def _notify_macos(title: str, message: str) -> bool:
    """
    Send notification on macOS using osascript.

    Args:
        title: Notification title.
        message: Notification body.

    Returns:
        True if successful, False otherwise.
    """
    try:
        script = f"display notification '{message}' with title '{title}'"
        subprocess.run(['osascript', '-e', script], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

