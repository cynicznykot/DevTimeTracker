"""Cross-platform notification system."""

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
    """
    system = platform.system()

    if system == 'Linux':
        return _notify_linux(title, message)
    elif system == 'Windows':
        return _notify_windows(title, message)
    elif system == 'Darwin':
        return _notify_macos(title, message)
    return False

