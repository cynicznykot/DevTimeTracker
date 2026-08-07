"""
Time tracking core module.

This module contains the main TimeTracker class that monitors user activity
in code editors and tracks the spent on different programming tasks.

It integrates with:
- Window manager to detect active windows
- Detector module to identify editors and languages
- Storage module to persist session data

Example:
    >>> from src.core.tracker import TimeTracker
    >>> tracker = TimeTracker(check_interval=10)
    >>> tracker.start()
"""

import time
from datetime import datetime
from typing import Optional

from src.core.window_manager import get_all_windows
from src.core.detectors import detect_editor
from src.storage.json_storage import JsonStorage


class TimeTracker:
    """
    Main time tracking class.

    This class monitors active windows to detect when the user is working
    in a code editor. It tracks time spent in editors and saves statistics
    to persistent storage.

    The tracker works by periodically checking active windows and recording
    sessions. A session begins when an editor window becomes active and ends
    when the user closes or minimizes the editor.

    Attributes:
        check_interval (int): How often to check for active windows (seconds).
        is_running (bool): Flag indicating if the tracker is currently running.
        current_editor (Optional[str]): Name of the currently active editor.
        session_start (Optional[datetime]): Start time of the current session.
        storage (JsonStorage): Storage for saving statistics.
    """

    def __init__(self, check_interval: int = 10, storage: Optional[JsonStorage] = None):
        """
        Initialize the time tracker.

        Args:
            check_interval: How often to check for active windows (seconds).
                            Default is 10 seconds.
            storage: Optional custom storage instance. If not provided,
                    a default JsonStorage will be created.
        """
        self.check_interval = check_interval
        self.is_running = False
        self.current_editor: Optional[str] = None
        self.session_start: Optional[datetime] = None
        self.storage = storage or JsonStorage()


    def _show_all_stats(self) -> None:
        """
        Display total statistics for all time.

        This method retrieves and displays the complete work statistics
        for all time, including total time per editor.
        """
        stats = self.storage.get_all_stats()

        if not stats:
            print("📊 No data all time.")
            return

        total = sum(stats.values())
        hours = total // 3600
        minutes = (total % 3600) // 60

        print(f"\n📊 TOTAL STATISTICS FOR ALL TIME:")
        print(f"Total time: {hours}h {minutes}m")

        print("\nBy editor:")
        for editor, seconds in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            h = seconds // 3600
            m = (seconds % 3600) // 60
            print(f"{editor}: {h}h {m}m")

    def _get_active_editor(self) -> Optional[str]:
        """
        Detect the currently active code editor.

        This method scans all open windows and returns the name of the
        first editor window found. It uses detect_editor() from the
        detectors module.

        Returns:
            The name of the active editor or None if no editor is found.
        """
        try:
            windows = get_all_windows()
            for window in windows:
                title = window.title
                if not title:
                    continue
                editor = detect_editor(title)
                if editor:
                    return editor
            return None
        except Exception:
            return None

    def _tick(self) -> None:
        """
        Perform one tracking tick.

        This method checks the active editor and manages the current session:
        - If an editor is found and no session exists, start a new session.
        - If an editor is found and a session exists, continue tracking.
        - If no editor is found and a session exists, end the session.
        """
        editor = self._get_active_editor()

        if editor:
            # Editor is open
            if self.current_editor is None:
                # Start a new session
                self.current_editor = editor
                self.session_start = datetime.now()
                print(f"▶️ Work in {editor} start")
        else:
            # Editor is closed
            if self.current_editor is not None and self.session_start is not None:

                # End the current session
                duration = int((datetime.now() - self.session_start).total_seconds())

                if duration >= 5:  # Minimum session duration (seconds)
                    today = datetime.now().strftime('%Y-%m-%d')
                    self.storage.add_time(today, self.current_editor, duration)

                    hours = duration // 3600
                    minutes = (duration % 3600) // 60
                    print(f"⏹️ Work in {self.current_editor} finished")
                    print(f"Duration: {hours}h {minutes}m")
                else:
                    print(f"⏭️ Session too short ({duration}s), skipped")

                self.current_editor = None
                self.session_start = None

    def start(self) -> None:
        """
        Start the time tracker.

        This method begins the tracking loop. It displays initial statistics
        and continues tracking until stopped by the user (Ctrl+C).

        The tracker wil check for active windows at regular intervals
        defined by check_interval.
        """
        self.is_running = True

        self._show_all_stats()
        print()

        print("🚀 Tracker start")
        print(f"📊 Check interval: {self.check_interval} seconds")
        print("Press Ctrl+C to stop\n")

        try:
            while self.is_running:
                self._tick()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            self.stop()

    def stop(self) -> None:
        """
        Stop the time tracker.

        This method ends the tracking loop, finishes any active session
        and displays final statistics.

        If there is an active session, it will be automatically completed
        and saved to storage.
        """
        self.is_running = False

        # Complete the current session if it exists
        if self.current_editor is not None and self.session_start is not None:
            duration = int((datetime.now() - self.session_start).total_seconds())
            if duration >= 5:
                today = datetime.now().strftime('%Y-%m-%d')
                self.storage.add_time(today, self.current_editor, duration)
                print(f"⏹️ Work in {self.current_editor} finished")

        print("\n👋 Tracker stopped")

        self._show_all_stats()