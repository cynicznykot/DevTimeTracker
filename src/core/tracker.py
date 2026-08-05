import time
from datetime import datetime
from typing import Optional

from src.core.window_manager import get_all_windows
from src.core.detectors import detect_editor, detect_language, extract_filename
from src.storage.json_storage import JsonStorage


class TimeTracker:
    def __init__(self, check_interval: int = 10, storage: Optional[JsonStorage] = None):
        self.check_interval = check_interval
        self.is_running = False
        self.current_editor: Optional[str] = None
        self.session_start: Optional[datetime] = None
        self.storage = storage or JsonStorage()
        self._show_today_stats()

    def _show_today_stats(self):
        today = datetime.now().strftime('%Y-%m-%d')
        stats = self.storage.get_daily_stats(today)

        if stats:
            total = sum(stats.values())
            hours = total // 3600
            minutes = (total % 3600) // 60
            print(f"📊 Today: {hours}ч {minutes}м")
            for editor, seconds in stats.items():
                h = seconds // 3600
                m = (seconds % 3600) // 60
                print(f"   {editor}: {h}ч {m}м")
        else:
            print("📊 Today: 0 minutes")

    def _show_all_stats(self):
        stats = self.storage.get_all_stats()

        if not stats:
            print("📊 No data all time")
            return

        total = sum(stats.values())
        hours = total // 3600
        minutes = (total % 3600) // 60

        print(f"\n📊 TOTAL ALL TIME:")
        print(f" All time: {hours}h {minutes}m")

        print("\n By editor:")
        for editor, seconds in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            h = seconds // 3600
            m = (seconds % 3600) // 60
            print(f" {editor}: {h}h {m}m")

    def _get_active_editor(self) -> Optional[str]:
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
        except Exception as e:
            print(f"⚠️ Error: {e}")
            return None

    def _tick(self):
        editor = self._get_active_editor()

        if editor:
            if self.current_editor is None:
                self.current_editor = editor
                self.session_start = datetime.now()
                print(f"▶️ Work in {editor} start")
        else:
            if self.current_editor is not None and self.session_start is not None:

                duration = int((datetime.now() - self.session_start).total_seconds())

                if duration >= 5:
                    today = datetime.now().strftime('%Y-%m-%d')
                    self.storage.add_time(today, self.current_editor, duration)

                    hours = duration // 3600
                    minutes = (duration % 3600) // 60
                    print(f"⏹️ Work in {self.current_editor} completed")
                    print(f"   Time: {hours}h {minutes}m")
                else:
                    print(f"⏭️ Short session ({duration}с), losted")

                self.current_editor = None
                self.session_start = None

    def start(self):
        self.is_running = True

        self._show_all_stats()
        print()

        print("🚀 Tracker start")
        print(f"📊 Inspection interval: {self.check_interval} second")
        print("Press Ctrl+C for stopping\n")

        try:
            while self.is_running:
                self._tick()
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.is_running = False

        if self.current_editor is not None and self.session_start is not None:
            duration = int((datetime.now() - self.session_start).total_seconds())
            if duration >= 5:
                today = datetime.now().strftime('%Y-%m-%d')
                self.storage.add_time(today, self.current_editor, duration)
                print(f"⏹️ Work in {self.current_editor} completed")

        print("\n👋 Tracker stopped")

        self._show_all_stats()