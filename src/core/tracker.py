import time
from datetime import datetime
from typing import Optional, Dict, Any

from src.core.window_manager import get_all_windows
from src.core.detectors import detect_editor, detect_language, extract_filename
from src.core.models import Session
from src.storage.json_storage import JsonStorage


class TimeTracker:
    def __init__(self, check_interval: int = 10, storage: Optional[JsonStorage] = None):
        self.check_interval = check_interval
        self.is_running = False
        self.current_session: Optional[Session] = None
        self.sessions: list = []
        self.storage = storage or JsonStorage()
        self._load_history()

    def _log_error(self, context: str, error: Exception):
        print(f"⚠️ [{context}] {error}")

    def _load_history(self):
        if self.storage:
            try:
                history = self.storage.load_sessions()
                self.sessions = history
                print(f"📂 Loaded {len(history)} sessions from history")
            except Exception as e:
                self._log_error("load_history", e)
                self.sessions = []
        else:
            self.sessions = []

    def _get_active_editor_info(self):
        try:
            windows = get_all_windows()

            for window in windows:
                title = window.title
                if not title:
                    continue
                editor = detect_editor(title)
                if editor:
                    return {
                        'editor': editor,
                        'language': detect_language(title),
                        'file': extract_filename(title),
                        'title': window.title,
                        'window': window
                    }
            return None

        except Exception as e:
            self._log_error("get_active_editor_info", e)
            return None

    def _tick(self):
        editor_info = self._get_active_editor_info()

        if editor_info:
            if self.current_session is None:
                self._start_session(editor_info)
            else:
                self._update_session(editor_info)
        else:
            if self.current_session is not None:
                self._end_session()

    def _start_session(self, editor_info):
        self.current_session = Session(
            editor=editor_info['editor'],
            language=editor_info['language'],
            file_path=editor_info['file'],
            start_time=datetime.now()
        )

        print(f"▶️ Session started: {editor_info['editor']}")
        if editor_info['file']:
            print(f"File: {editor_info['file']}")
        if editor_info['language']:
            print(f"Language: {editor_info['language']}")
        print()

    def _end_session(self):
        if self.current_session is None:
            return

        self.current_session.end_time = datetime.now()
        duration = self.current_session.get_duration()

        self.sessions.append(self.current_session)

        if self.storage:
            try:
                self.storage.save_session(self.current_session)
            except Exception as e:
                print(f"⚠️ Save session error: {e}")

        print(f"⏹️ Finished Session: {self.current_session.editor}")
        print(f"Duration: {duration // 60} minutes {duration % 60} seconds")
        print()

        self.current_session = None

    def _update_session(self, editor_info):
        if self.current_session is None:
            return

        if (self.current_session.file_path != editor_info['file'] or
            self.current_session.language != editor_info['language']):
            self._end_session()
            self._start_session(editor_info)

    def _show_summary(self):
        all_sessions = self.sessions.copy()

        if not all_sessions:
            print(f"No sessions found.")
            return

        total_time = sum(s.get_duration() for s in all_sessions)
        hours = total_time // 3600
        minutes = (total_time % 3600) // 60

        print("\n📊 TOTAL STATISTICS:")
        print(f" Total time: {hours}h {minutes}m")
        print(f" Total sessions: {len(all_sessions)}")

        daily_stats = {}
        for session in all_sessions:
            date = session.start_time.date()
            daily_stats[date] = daily_stats.get(date, 0) + session.get_duration()

        print("\n📅 By day:")
        for date, duration in sorted(daily_stats.items(), reverse=True):
            h = duration // 3600
            m = (duration % 3600) // 60
            print(f"   {date}: {h}ч {m}м")

        editor_stats = {}
        for session in all_sessions:
            editor = session.editor
            editor_stats[editor] = editor_stats.get(editor, 0) + session.get_duration()

        if editor_stats:
            print("\n🖥️ By editor:")
            for editor, duration in sorted(editor_stats.items(), key=lambda x: x[1], reverse=True):
                h = duration // 3600
                m = (duration % 3600) // 60
                print(f" {editor}: {h}h {m}m")

    def start(self):
        self.is_running = True
        print(f"🚀 Tracker is running.")
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

        if self.current_session:
            self._end_session()

        if self.storage and self.sessions:
            try:
                self.storage.save_sessions(self.sessions)
            except Exception as e:
                print(f"⚠️ Error saving sessions: {e}")

        print(f"\n 👋 Tracker stopped.")
        print(f"📈 History sessions: {len(self.sessions)}")
        self._show_summary()


