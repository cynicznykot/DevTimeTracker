from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Session:
    editor: str
    language: Optional[str]
    file_path: Optional[str]
    start_time: datetime
    end_time: Optional[datetime] = None

    def get_duration(self):
        end = self.end_time or datetime.now()
        return int((end - self.start_time).total_seconds())

