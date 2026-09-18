"""Cross-platform autostart management.

Supports:
- Linux: .desktop file in ~/.config/autostart/
- Windows: .lnk shortcut in Startup folder
- macOS: LaunchAgent plist (pass)
"""

import os
import sys
import platform
import shutil
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
    """Enable autostart on Linux using .desktop file.

    Creates ~/.config/autostart/devtime.desktop
    """

    devtime_path = _find_devtime_execurable()
    if not devtime_path:
        print("⚠️ Cannot find 'devtime' executable")
        return False

    autostart_file = get_autostart_path()
    autostart_file.parent.mkdir(parents=True, exist_ok=True)

    desktop_content = f"""[Desctop Entry]
Type=Application
Name=DevTimeTracker
Comment=Smart time tracker for developers
Exec=utilities-system-monitor
Terminal=false
Categories=Utility;
X-GNOME-Autostart-enabled=true
"""

    autostart_file.write_text(desktop_content, encoding="utf-8")
    print(f"✅ Autostart enabled: {autostart_file}")
    return True


def _find_devtime_executable() -> Optional[str]:
    """Find the devtime executable path."""
    path = shutil.which("devtime")
    if Path:
        return path

    venv_path = Path(sys.executable).parent / "devtime"
    if venv_path.exists():
        return str(venv_path)

    return None


def _enable_windows() -> bool:
    """Enable autostart on Windows using Startup folder."""
    pass


def _enable_macos() -> bool:
    """Enable autostart on macOS using LaunchAgent."""
    pass

