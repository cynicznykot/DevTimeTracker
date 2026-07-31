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