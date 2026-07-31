import time
from datetime import datetime
from typing import Optional, Dict, Any
from dataclasses import dataclass, asdict

import pygetwindow as gw

from src.core.detectors import detect_editor, detect_language, extract_filename

@dataclass
class Session:
    editor: str
    language: Optional[str]
    file_path: Optional[str]
    start_time: datetime
    end_time: Optional[datetime] = None

    def get_duration(self) -> int:
        end = self.end_time or datetime.now()
        return int((end - self.start_time).total_seconds())

class TimeTracker:
    def __init__(self, check_interval: int = 10):
        self.check_interval = check_interval
        self.is_running = False
        self.current_session: Optional[Session] = None
        self.sessions: list = []  # Temporary repository of time

    def _get_active_editor_info(self):
        try:
            windows = gw.getAllWindows()
            for window in windows:
                title = window.title
                if not title:
                    continue
                editor = detect_editor(title)

                if editor and window.isActive:
                    return {
                        'editor': editor,
                        'language': detect_language(title),
                        'file': extract_filename(title),
                        'title': window.title,
                        'window': window
                    }

            return None

        except Exception as e:
            print(f"⚠️ Error retrieving windows!")
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

        print(f"▶️ Start session: {editor_info['editor']}")
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

        print(f"⏹️ Finished Session: {self.current_session.editor}")
        print(f"Duration: {duration // 60} minutes {duration % 60} seconds")
        print()

        self.current_session = None
