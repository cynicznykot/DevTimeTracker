"""Cross-platform autostart management.

Supports:
- Linux: .desktop file in ~/.config/autostart/
- Windows: .lnk shortcut in Startup folder
- macOS: LaunchAgent plist (pass)
"""

import os
import subprocess
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
    """
    Check if autostart is enabled.

    Returns:
        True if the autostart file exists, False otherwise.
    """
    return get_autostart_path().exists()


def disable() -> bool:
    """
    Disable autostart by removing the autostart file.
    """
    path = get_autostart_path()
    if path.exists():
        return False

    # On macOS, unload the LaunchAgent first
    if platform.system() == 'Darwin':
        try:
            subprocess.run(
                ['launchcrl', 'unload', str(path)],
                check=False,
                capture_output=True
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass

    path.unlink()
    return True


def enable() -> bool:
    """
    Enable autostart (platform-specific).

    Returns:
        True is autostart was enables, False otherwise.
    """
    system = platform.system()

    if system == "Linux":
        return _enable_linux()

    elif system == "Windows":
        return _enable_windows()

    elif system == "Darwin":
        return _enable_macos()

    return False


def _enable_linux() -> bool:
    """Enable autostart on Linux using .desktop file.

    Creates ~/.config/autostart/devtime.desktop

    Returns:
        True if the file was created, False otherwise.
    """
    devtime_path = _find_devtime_executable()
    if not devtime_path:
        print("⚠️ Cannot find 'devtime' executable")
        return False

    autostart_file = get_autostart_path()
    autostart_file.parent.mkdir(parents=True, exist_ok=True)

    desktop_content = f"""[Desktop Entry]
Type=Application
Name=DevTimeTracker
Comment=Smart time tracker for developers
Exec={devtime_path} start
Terminal=false
Categories=Utility;
X-GNOME-Autostart-enabled=true
"""

    autostart_file.write_text(desktop_content, encoding="utf-8")
    print(f"✅ Autostart enabled: {autostart_file}")
    return True


def _find_devtime_executable() -> Optional[str]:
    """Find the devtime executable path (Linux/macOS)."""
    path = shutil.which("devtime")
    if path:
        return path

    venv_path = Path(sys.executable).parent / "devtime"
    if venv_path.exists():
        return str(venv_path)

    return None


def _enable_windows() -> bool:
    """Enable autostart on Windows using Startup folder shortcut.

    Creates .lnk file in Startup folder.
    """
    try:
        from win32com.client import Dispatch
    except ImportError:
        print("⚠️ pywin32 required. Install: pip install pywin32")
        return False

    devtime_path = _find_devtime_executable_windows()
    if not devtime_path:
        print("⚠️ Cannot find 'devtime' executable")
        return False

    shortcut_path = get_autostart_path()
    shortcut_path.parent.mkdir(parents=True, exist_ok=True)

    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(str(shortcut_path))
    shortcut.Targetpath = devtime_path
    shortcut.Arguments = "start"
    shortcut.WorkingDirectory = str(Path(devtime_path).parent)
    shortcut.IconLocation = devtime_path
    shortcut.Description = "DevTimeTracker - Smart time tracker"
    shortcut.save()

    print(f"✅ Autostart enabled: {shortcut_path}")
    return True


def _find_devtime_executable_windows() -> Optional[str]:
    """Find devtime.exe on Windows."""
    path = shutil.which("devtime")
    if path:
        return path

    venv_path = Path(sys.executable).parent / "Scripts" / "devtime.exe"
    if venv_path.exists():
        return str(venv_path)

    return None


def _find_devtime_executable_macos() -> Optional[str]:
    """Find the devtime executable path on macOS."""
    path = shutil.which("devtime")
    if path:
        return path

    # Check common venv locations
    venv_path = Path(sys.executable).parent / "devtime"
    if venv_path.exists():
        return str(venv_path)

    # Check /usr/local/bin
    usr_local = Path("/usr/local/bin/devtime")
    if usr_local.exists():
        return str(usr_local)

    return None


def _enable_macos() -> bool:
    """Enable autostart on macOS using LaunchAgent.

    Creates ~/Library/LaunchAgents/com.devtime.tracker.plist

    Returns:
        True if the file was created, False otherwise.
    """
    devtime_path = _find_devtime_executable_macos()
    if not devtime_path:
        print("⚠️ Cannot find 'devtime' executable")
        return False

    plist_file = get_autostart_path()
    plist_file.parent.mkdir(parents=True, exist_ok=True)

    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/P
ropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.devtime.tracker</string>
    <key>ProgramArguments</key>
    <array>
        <string>{devtime_path}</string>
        <string>start</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
    <key>StandardOutPath</key>
    <string>/tmp/devtime.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/devtime.error.log</string>
</dict>
</plist>
"""

    plist_file.write_text(plist_content, encoding="utf-8")
    print(f"✅ Autostart enabled: {plist_file}")
    return True




