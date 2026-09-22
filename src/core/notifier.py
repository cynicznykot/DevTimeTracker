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


def _notify_linux(title: str, message: str) -> bool:
    """Send notification on Linux using notify-send."""
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
    """Send notification on Windows using win10toast."""
    try:
        from win10toast import ToastNotifier
        toaster = ToastNotifier
        toaster.show_toast(title, message, duration=5, threaded=True)
        return True
    except ImportError:
        return False


def _notify_macos(title: str, message: str) -> bool:
    """Send notification on macOS using osascript."""
    try:
        script = f"display notofication '{message}' with title '{title}'"
        subprocess.run(['osascript', '-e', script], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

